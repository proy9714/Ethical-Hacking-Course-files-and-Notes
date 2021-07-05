#!/usr/bin/env python
import scapy.all as scapy

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    ans = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return ans[0][1].hwsrc

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    # If the packet sniffed is a ARP Response
    # op = 2 is of type "is-at"
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op==2:
        try:
            # This is the actual mac address 
            real_mac = get_mac(packet[scapy.ARP].psrc)
            # This is the mac as visible in the sniffed ARP packet 
            response_mac = packet[scapy.ARP].hwsrc
            
            if real_mac != response_mac:
                print("You are under attack!")
            
        except IndexError:
            pass
        
try:
    print("Sniffing...")
    sniff("eth0")
    
except KeyboardInterrupt:
    print('Quitting arpspoof detector')
    raise KeyboardInterrupt
