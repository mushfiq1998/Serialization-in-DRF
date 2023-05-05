# Import a python module or package
import requests

# URl for getting a single model object.
URL = "http://127.0.0.1:8000/studentinfo/1"

# URl for getting queryset.
# URL = "http://127.0.0.1:8000/studentinfo"

response = requests.get(url = URL)
# Extract JSON data from response object that is stored 
# in the variable 'json_data'.
json_data = response.json()
# Show JSON data in terminal. 
print(json_data)
