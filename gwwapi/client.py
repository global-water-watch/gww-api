# -*- coding: utf-8 -*-

import datetime

import geopandas as gpd
import pandas as pd
import requests
from shapely.geometry import shape

base_url = "https://api.globalwaterwatch.earth"
start = datetime.datetime(2010, 1, 1)
stop = datetime.datetime(2022, 1, 1)

# All functions making server requests
def _check_request(r):
    """ Checks request """
    try:
        r.raise_for_status()
    except requests.RequestException as e: 
        print(e)
        print(r.text)
        raise e

def get_reservoirs(skip=1, limit=5):
    """
    Gets reservoirs from API. Return list of reservoirs. Each list element is a dict representing a reservoir. The dict will contain the reservoir geometry and a set of reservoir properties. 
    
    Args:
        skip (int): How many reservoir to skip
        limit (int): Max number of reservoirs that will be returned.
    
    Returns: 
        reservoirs (list)
    """

    
    url = f"{base_url}/reservoir"
    params = {
        "skip": skip,
        "limit": limit,
    }

    r = requests.get(url, params=params, timeout=2)
    _check_request(r)
    return(r)

def get_reservoir_by_id(reservoir_id:int):
    """
    Get reservoir (geometry and props) by ID.
    
    Args: 
        reservoir_id (int): Global Water Watch ID. 
    
    Returns: 
        requests.models.Response: Raw response object.

    """
    

    url = f"{base_url}/reservoir/{reservoir_id}"
    
    r = requests.get(url)
    _check_request(r)
    return(r)
        
def get_reservoirs_by_geom(geom:str):
    """
    For a geometry, return the list of reservoirs in that geometry. Each element in the list is a dict containing reservoir geometry and properties.

    Args: 
        geom (str)
    
    Returns: 
        reservoirs (list)
    """
    
    url = f"{base_url}/reservoir/geometry"
    # do post request to end point with the serialized geometry as post data
    r = requests.post(url, data=geom)
    _check_request(r)
    return(r.json())

def get_reservoir_ts(reservoir_id, start=start, stop=stop):
    """
    Get time series data for reservoir with given ID. This will return raw data. If you want to obtain post-processed monthly data, use the get_reservoir_ts_monthly function instead. 
    
    Args: 
        reservoir_id (str): Global Water Watch Reservoir ID
        start (datetime.datetime()): Start 
        stop (datetime.datetime()): Stop
    
    Returns: 
        requests.models.Response: Raw response object.
    """
    url = f"{base_url}/reservoir/{reservoir_id}/ts/surface_water_area"
    params = {
        "start": start.strftime("%Y-%m-%dT%H:%M:%S"),
        "stop": stop.strftime("%Y-%m-%dT%H:%M:%S")
    }
    
    r = requests.get(url, params=params)
    _check_request(r)
    return(r)

def get_reservoir_ts_monthly(reservoir_id:int, start=start, stop=stop):
    """
    Get monthly time series data for reservoir with given ID. Monthly time series data is post-processed from the raw data. If you want to obtain the raw data, use the get_reservoir_ts function instead. 
    
    Args: 
        reservoir_id (str): Global Water Watch Reservoir ID
        start (datetime.datetime()): Start 
        stop (datetime.datetime()): Stop
    
    Returns: 
        requests.models.Response: Raw response object.
    """
    

    url = f"{base_url}/reservoir/{reservoir_id}/ts/surface_water_area_monthly"
    params = {
        "start": start.strftime("%Y-%m-%dT%H:%M:%S"),
        "stop": stop.strftime("%Y-%m-%dT%H:%M:%S")
    }
    
    r = requests.get(url, params=params)
    _check_request(r)
    return(r)

# Utils
def to_geopandas(data):
    """
    Ingests list of reservoirs and converts into a geopandas GeoDataFrame for further analyses
    
    """
    geoms = [shape(f["geometry"]) for f in data]
    props = [{**f["properties"], **{"id": f["id"]}} for f in data]
    return gpd.GeoDataFrame(props, geometry=geoms, crs=4326)

def to_timeseries(data, name=None):
    """
    Convert raw list of jsons to organized pandas.DataFrame
    """
    if name is None:
        name = "area"

    t_index = pd.to_datetime([p["t"] for p in data])
    v = [{name: p["value"]} for p in data]

    return pd.DataFrame(
        v,
        index=pd.DatetimeIndex(t_index).date)
