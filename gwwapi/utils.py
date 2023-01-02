# -*- coding: utf-8 -*-

import datetime
import geopandas as gpd
import pandas as pd
import requests
from shapely.geometry import shape

# Utils
def to_geopandas(data:list):
    """
    Ingests list of reservoirs and converts into a geopandas GeoDataFrame for further analyses.

    Args: 
        data (list): List 
    
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

    t_index = [p["t"] for p in data]
    v = [{name: p["value"]} for p in data]
    pd.DatetimeIndex(t_index)
    return pd.DataFrame(
        v,
        index=pd.DatetimeIndex(t_index).date)