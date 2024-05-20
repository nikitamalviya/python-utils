# ! pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -U requests, pprint, rich

import requests
from pprint import pprint
from rich import print_json


# sort the dictionary key's values and pretty print the text    
classes_count = {}
classes_count = sorted(classes_count.items(), key=lambda item: item[1], reverse=True)
click.secho(f"Sorted dictionary : ", fg="green")
pprint(classes_count)

with open(image_path, 'rb') as f:
    multipart_form_data = {'file':  f}
    response = requests.post(url=url, files=multipart_form_data, verify=False) # data= {"source":"test"}, 
    response = response.json()
    pretty_response = json.dumps(response, indent=4)
    print_json(pretty_response)
