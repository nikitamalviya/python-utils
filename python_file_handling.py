import json, pprint

# read JSON file
def read_json_file(file_path):
  with open(file_path, 'r') as file:
    json_data=json.load(file)
    pprint.pprint(json_data, compact=True)
    return json_data
    
