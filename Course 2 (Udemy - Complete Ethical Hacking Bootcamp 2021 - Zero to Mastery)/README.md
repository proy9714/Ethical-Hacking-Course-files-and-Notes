# General Commands

| Command | Description |
| --- | --- |
| locate | Outputs the path of concerned filename |

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

	.rb : Extension for ruby 

> ***Can run regular terminal commands within metasploit as well***

| Metasploit commands | Description |
| --- | --- |
| show *option* | Shows all option |
|show *modulename* | Display all available *module options/files* |
| use *modulename*/*file* | Using a file in a module |
| show info | Shows the information and details about a particular module file **(|Run after *use* command)** |
| show options | Shows module options **(|Run after *use* command)** |
| show *targets* | Displays all targets which can be exploited |
| set *option* | Sets a particular option |
| set *LHOST/RHOST* | Setting LHOST or RHOST ip |
| show *payloads* | Display possible payloads/ payloads for a particular exploit |
| set *payload* | Change payload for exploit |
| set *target* | Set target type *(Not ip, but a type of target for eg. Windows XP)* |