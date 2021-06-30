import socket
import termcolor

closed_ports = 0
def scan(target, ports):
	print('\n' + ' Starting Scan For ' + str(target))
	global closed_ports
	closed_ports = 0
	for port in range(1,ports):
		scan_port(target,port)
	if closed_ports!=0:
		print(termcolor.colored(("[*]Closed ports = " + str(closed_ports)), "red"))


def scan_port(ipaddress, port):
	try:
		#Socket object
		sock = socket.socket()

		#Using socket object to connect
		sock.connect((ipaddress, port))
		
		# Prints success message on establishing connection
		print("[+] Port Opened " + str(port))
		
		sock.close()
	except:
		global closed_ports
		closed_ports = closed_ports + 1
		#print("[-] Port Closed " + str(port))


targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)
