# ! pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -U requests, pprint, rich

import requests
from pprint import pprint
from rich import print_json

# pretty print a dict
pprint(dict_name)

############# 
# pretty print API JSON response 
with open(image_path, 'rb') as f:
    multipart_form_data = {'file':  f}
    response = requests.post(url=url, files=multipart_form_data, verify=False) # data= {"source":"test"}, 
    response = response.json()
    pretty_response = json.dumps(response, indent=4)
    print_json(pretty_response)
