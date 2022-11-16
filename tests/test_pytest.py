import pytest 
from gwwapi import client as cli

class TestClass:
    def test_get_reservoirs(skip=50, limit=2):
        # test if reservoir is retrieved and has the expected id
        r = cli.get_reservoirs(skip=50, limit=2)
        gdf = cli.to_geopandas(r.json())
        assert(gdf.iloc[0]["id"] == 58)

    def test_get_reservoir_ts(id=3001):
        # test if reservoir ts is retreived and has expected column header
        assert cli.get_reservoir_ts(3001).json()[0]['name'] == 'surface_water_area_monthly'


