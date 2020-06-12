#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import urlparse

def request(url):
    try: 
        return requests.get(url)
    except requests.exceptions.ConnectionError: 
        pass

target_url = "http://10.0.2.11/mutillidae/index.php?page=dns-lookup.php"
response = request(target_url)

# Parsing the html page 
parsed_html = BeautifulSoup(response.content, features="html.parser")

# Extracting all the forms on the page
# Using findAll() to get all HTML elements
forms_list = parsed_html.findAll("form")

for form in forms_list:
    # Extracting the action attribute value from the form tag
    # Using get() to get the value of a property in a tag
    action = form.get("action")
    
    # Concatinating the action to get complete path
    post_url = urlparse.urljoin(target_url, action)
    print("Action url = " + post_url)
    
    method = form.get("method")
    print("Method = " + method)

    inputs_list = form.findAll("input")
    post_data = {}
    for inputtag in inputs_list:
        input_name = inputtag.get("name")
        input_type = inputtag.get("type")
        input_value = inputtag.get("value")

        if input_type == "text":
            input_value = "test"

        post_data[input_name] = input_value

    result = requests.post(post_url, post_data)
    print(result.content)