import json

with open('zips_us_topo.json') as data_file:    
    data = json.load(data_file)
    for geom in data["objects"]["zip_codes_for_the_usa"]["geometries"]:
    	print geom["properties"]["zip"]
	break



    

