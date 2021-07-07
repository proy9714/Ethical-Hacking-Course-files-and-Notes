# General Commands

| Command | Description |
| --- | --- |
| locate | Outputs the path of concerned filename |
| telnet *ip* | Connect to *ip* via telnet |
| sudo su | Getting to root |
| ssh *username@ip* | Connect via ssh to *ip* |
| hostname | Get the name of the host machine |
| vncviwere *ip* | Connect to vnc |
| getuid | Get user id on windows |

# Reconnaissance and Information gathering

| Command | Description |
| --- | --- |
| nslookup | Lookup ip address |
| whois | ip/domain details |
| whatweb | web scanner to scan hosts |
| theHarvester | email gathering |
| hunter.io | website for email gathering |
| redhawk | website information gathering |
| sherlock | find accounts across social media using username |
| arp | manipulate the system arp cache |


# Scanning

| Command | Description |
| --- | --- |
| netdiscover | For discovering available networks/ips |
| netstat | (Obsolete) Use ss |
| nmap | Scanning for ports |

---

***Nmap options***

	-sS : Syn Scan, half open scanning...detecting replies from syn tcp packets
	-sF : Fyn scan (?)
	-sV : Version number
	--version-intensity : 0 to 9, default:7
	-A : Aggressive
	-sn : No port can, like netdiscover
	-p : port range/ single port scan
	-p- : Scan all 65535 ports
	>> filename : to save output to file
	-oN : Output scan in normal file
	-f : Small fragmented tcp packets
	-D : decoys, Make it appear to the target as if multiple ips have scanned target (for hiding attacker ip)
	-S : spoof your ip address, but results of scan sent to spoofed ip
	-Pn : Doesn't perform ping scan, assumes all hosts are online (HAVE to use the -S)
	-e : A network interface (eg: eth0)
	-g : Source port (Maybe to bypass firewall)
	-T : Timing template
	-F: Fast mode - Scan fewer ports than the default scan

# Vulnerability Analysis

| Command | Description |
| --- | --- |
| nmap scripts | For finding vulnerabilities, explore documentation of nmap on internet |
| searchsploit | exploiting vulnerabilities |
| Nessus | Software for vulnerability analysis *(Only local ip addresses, atleast with the free version)* |

---

***Nmap Scripts***

	nmap scripts are in directory: usr/share/nmap/scripts
	
	nmap --script scriptgroup

	Script help: nmap --script-help scriptname 

# Exploitation and Gaining access

## Metasploit Framework

Starting Metasploit Framework: **msfconsole**

Navigating to Metasploit framework directory: cd /user/share/metaspolit-framework

Types of modules are in : /user/share/metaspolit-framework/modules

| Metasploit Modules | Description |
| --- | --- |
| auxiliary | Does not execute a payload. Helps in performing scanning, fuzzing, dos etc. Actions performed in inital steps of hacking |
| encoders | Help in avoiding antivirus (Not very useful nowadays) |
| evasion | Generally used to bypass windows defender (Although maybe not very useful now) |
| exploits | Exploiting vulnerabilities of target system |
| nops | Instruction for the processor to do nothing. Useful for buffer overflow. *NOP - (No Operation)* |
| payloads | For delivering payloads to target |
| post | Post exploitation. For gathering or stealing information etc. |

---

***payloads***
	
	singles : Standalone payload
	
	stagers : Setting up network connection between target and attacker. Designed to be small and reliable.
	
	stages : Payload components that are downloaded by stagers modules. Can provide advanced features with no size limits, eg. meterpreter shells.

***Note***

	bind : Direct connection
	
	reverse : reverse connection

	.rb : Extension for ruby, Generaally exploit files	
	
	multi/ : Can be run against multiple OS

> ***Can run regular terminal commands within metasploit as well***

| Metasploit commands | Description |
| --- | --- |
| show *option* | Shows all option |
|show *modulename* | Display all available *module options/files* |
| use *modulename*/*file* | Using a file in a module |
| show info | Shows the information and details about a particular module file **(Run after *use* command)** |
| show *options* | Shows module options **(Run after *use* command)** |
| show *targets* | Displays all targets which can be exploited |
| set *option* | Sets a particular option |
| set *LHOST/RHOST* | Setting LHOST or RHOST ip |
| show *payloads* | Display possible payloads/ payloads for a particular exploit |
| set *payload* | Change payload for exploit |
| set *target* | Set target type *(Not ip, but a type of target for eg. Windows XP)* |
| search *software name* | To search for exploit for the software eg: search vdftpd|
| exploit | Start the exploit |
| exit | Exit the shell/ End exploit |
| run | Run a module file |
| sessions | Check all available shells |
| sessions -i *session id* | Enter session |


## NETCAT

netcat is a simple unix utility which reads and writes data across net‐work connections, using TCP or UDP protocol. In  the  simplest usage, "nc host port" creates a TCP connection to the given port on the given target host. 

| Netcat commands | Description |
| --- | --- |
| nc -h | help |

## METERPRETER

| Meterpreter commands | Description |
| --- | --- |
| help | Open help |


***Eternalblue***

	Exploit smb vulnerability on windows

	Available on metasploit framework

	Works on 64bit windows, Crashes 32bit windows

***DoublePulsar***

	Read details on Rapid7 website

	Can work on both 32bit and 64bit systems

	Obtain from Github

	Copy files to metasploit directory to add it to the framework

	Copy all files to root directory

	Need Wine to run

		Run as root

		sudo dpkg --add-architecture i386
		
		apt-get update
		
		apt-get install wine32

	Change PROCESSINJECT ot lsass.exe if attack against 64bit machine

	Change TARGETARCHITECTURE to x64 if attack against 64bit machine

	Change payload to windows/x64/meterpreter/reverse_tcp if attack against 64bit machine

***Bluekeep***

	Windows XP to Windows 7 Exploit
	
	Port 3389 (RDC : Remote Desktop Protocol) needs to be enabled on target

	To enable RDC on Windows : Control Panel -> System and Settings -> Remote Desktop -> Enable

***Routersploit***

	Hacking router

	Download from Github