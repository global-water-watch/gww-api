# -*- coding: utf-8 -*-

import datetime
import pandas as pd
import requests
from shapely.geometry import shape

# Defaults
base_url = "https://api.globalwaterwatch.earth"
start = datetime.datetime(2000, 1, 1)
stop = datetime.datetime(2023, 1, 1)


# Check request function
def _check_request(r):
    """Checks request"""
    try:
        r.raise_for_status()
    except requests.RequestException as e:
        print(e)
        print(r.text)
        raise e


# Get Requests
def get_reservoirs(skip=1, limit=5):
    """
    Gets reservoirs from API. Return a FeatureCollection of reservoirs.

    Args:
        skip (int): How many reservoir to skip
        limit (int): Max number of reservoirs that will be returned.

    Returns:
        dictionary with FeatureCollection.
    """

    url = f"{base_url}/reservoir"
    params = {
        "skip": skip,
        "limit": limit,
    }

    r = requests.get(url, params=params, timeout=2)
    _check_request(r)
    return r.json()


def get_reservoir_by_id(reservoir_id: int):
    """
    Get reservoir (geometry and props) by ID.

    Args:
        reservoir_id (int): Global Water Watch ID.

    Returns:
        dict: containing reservoir geometry and properties

    """

    url = f"{base_url}/reservoir/{reservoir_id}"

    r = requests.get(url)
    _check_request(r)
    return r.json()


def get_reservoir_ts(reservoir_id: int, start=start, stop=stop):
    """
    Get time series data for reservoir with given ID. This will return raw data. If you want to obtain post-processed monthly data, use the get_reservoir_ts_monthly function instead.

    Args:
        reservoir_id (str): Global Water Watch Reservoir ID
        start (datetime.datetime()): Start
        stop (datetime.datetime()): Stop

    Returns:
        list: containing dictionaries with time, value, unit and variable name of the reservoir time series
    """
    url = f"{base_url}/reservoir/{reservoir_id}/ts/surface_water_area"
    params = {
        "start": start.strftime("%Y-%m-%dT%H:%M:%S"),
        "stop": stop.strftime("%Y-%m-%dT%H:%M:%S"),
    }

    r = requests.get(url, params=params)
    _check_request(r)
    return r.json()


def get_reservoir_ts_monthly(reservoir_id: int, start=start, stop=stop):
    """
    Get monthly time series data for reservoir with given ID. Monthly time series data is post-processed from the raw data. If you want to obtain the raw data, use the get_reservoir_ts function instead.

    Args:
        reservoir_id (str): Global Water Watch Reservoir ID
        start (datetime.datetime()): Start
        stop (datetime.datetime()): Stop

    Returns:
        list: containing dictionaries with time, value, unit and variable name of the reservoir time series
    """

    url = f"{base_url}/reservoir/{reservoir_id}/ts/surface_water_area_monthly"
    params = {
        "start": start.strftime("%Y-%m-%dT%H:%M:%S"),
        "stop": stop.strftime("%Y-%m-%dT%H:%M:%S"),
    }

    r = requests.get(url, params=params)
    _check_request(r)
    return r.json()


# Post Requests
def get_reservoirs_by_geom(geom: str):
    """
    For a geometry, return the FeatureCollection of reservoirs in that geometry.

    Args:
        geom (str)

    Returns:
        list: List containing all reservoirs
    """

    url = f"{base_url}/reservoir/geometry"
    # do post request to end point with the serialized geometry as post data
    r = requests.post(url, data=geom)
    _check_request(r)
    return r.json()


def get_reservoir_ts_monthly_by_geom(geom: str, start=start, stop=stop):
    """
    For a geometry, return all monthly timeseries within that geometry.


    Args:
        geom (str): Input Geometry
        start (datetime.datetime()): Start
        stop (datetime.datetime()): Stop

    Returns:
        list: List containing monthly surface water area time series for all reservoirs within the geometry
    """

    url = f"{base_url}/reservoir/geometry/ts/surface_water_area"

    params = {
        "agg_period": "monthly",
        "start": start.strftime("%Y-%m-%dT%H:%M:%S"),
        "stop": stop.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    # do post request to end point with the serialized geometry as post data
    r = requests.post(url, params=params, data=geom)
    # _check_request(r)
    return r.json()
