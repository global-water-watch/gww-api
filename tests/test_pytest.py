import pytest 
from gwwapi import client as cli 
from gwwapi import utils 
import json 

class TestClass:
    def test_get_reservoirs(skip=50, limit=2):
        # test if reservoir is retrieved and has the expected id
        r = cli.get_reservoirs(skip=50, limit=2)
        gdf = utils.to_geopandas(r)
        assert gdf.iloc[0]["id"] == 60

    def test_get_reservoir_ts(id=3001):
        # test if reservoir ts is retreived and has expected column header
        assert cli.get_reservoir_ts(3001)[0]['name'] == 'surface_water_area'

    def test_get_reservoirs_by_geom(geom):
        
        geom = json.dumps({
            "type": "Polygon",
            "coordinates": [
                [
                [
                    15.97412109375,
                    49.0880329436187
                ],
                [
                    16.194190979003906,
                    49.0880329436187
                ],
                [
                    16.194190979003906,
                    49.20503726723141
                ],
                [
                    15.97412109375,
                    49.20503726723141
                ],
                [
                    15.97412109375,
                    49.0880329436187
                ]
                ]
            ]
        })
        
        r = cli.get_reservoirs_by_geom(geom)
        assert 'id' in r[0].keys()
        assert r[0]['id'] == 60841