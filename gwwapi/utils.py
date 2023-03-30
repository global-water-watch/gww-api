# -*- coding: utf-8 -*-

import geopandas as gpd
import pandas as pd
from shapely.geometry import shape


# Utils
def to_geopandas(data: list):
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

    t_index = pd.to_datetime([p["t"] for p in data])
    v = [{name: p["value"]} for p in data]

    return pd.DataFrame(v, index=t_index.date)
