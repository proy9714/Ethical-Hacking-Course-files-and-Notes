#!/usr/bin/env python

import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP/ IP range")
    options = parser.parse_args()
    return options

def scan(ip):
    # ARP packet with source ip as ip
    arp_request = scapy.ARP(pdst=ip)
    # arp_request.show()

    # Destination mac address set to broadcast mac address
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # broadcast.show()

    # Combining the ARP packet with the broadcast MAC address
    arp_request_broadcast = broadcast / arp_request

    # ans, unans = scapy.srp(arp_request_broadcast, timeout=1)
    # Here ans = (packet sent, answer from received host)
    ans = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in ans:
        # The show() function displays the data in the packet
        # print(element[1].show())

        # IP and MAC of client who replies back to sent ARP
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
        # print(element[1].psrc + "\t\t" + element[1].hwsrc)

    return clients_list

    # print(ans.summary())
    # print(unans.summary())

    # arp_request_broadcast.show()

    # print(arp_request.summary())
    # scapy.ls(scapy.ARP())
    # scapy.ls(scapy.Ether())

def print_result(results_list):
    if results_list.__len__()!=0:
        print("IP\t\t\tMAC Address")
        print("\n---------------------------------------------")
        for client in results_list:
            print(client["ip"] + "\t\t" + client["mac"])


options = get_arguments()
#scan_result = scan("10.0.2.1/24")
scan_result = scan(options.target)
print_result(scan_result)
