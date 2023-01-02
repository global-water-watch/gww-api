import pytest 
from gwwapi import client as cli 
from gwwapi import utils 
import json 

# WIP
# import os 

# input_data_dir = os.path.join(dirname(abspath(__file__)), "data")
# input_data_file = os.path.join(input_data_dir, 'basins.geojson')

# with open(input_data_file,'r') as f:
#     data = json.loads(f.read())
# _data = data['features'][1]['geometry']
# _geom = json.dumps(_data)

class TestClass:
    def test_get_reservoirs(skip=50, limit=2):
        # test if reservoir is retrieved and has the expected id
        r = cli.get_reservoirs(skip=50, limit=2)
        gdf = utils.to_geopandas(r.json())
        assert gdf.iloc[0]["id"] == 60

    def test_get_reservoir_ts(id=3001):
        # test if reservoir ts is retreived and has expected column header
        assert cli.get_reservoir_ts(3001).json()[0]['name'] == 'surface_water_area'
