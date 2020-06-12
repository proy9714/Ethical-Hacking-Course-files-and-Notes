#!/usr/bin/env python

import requests

# Target url is the URL in the action field of the form tag
### AGAINST METASPLOITABLE ###
target_url = "http://10.0.2.11/dvwa/login.php"

# The first field is the name of the field in the input tag
data_dict = {"username": "admin", "password": "password", "Login":"submit"}

response = requests.post(target_url, data=data_dict)
print(response.content)