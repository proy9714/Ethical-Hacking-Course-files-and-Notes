#!/usr/bin/env python

# iptables -I FORWARD -j NFQUEUE --queue-num 0
# iptables --flush

from netfilterqueue import NetfilterQueue


def pkt_filter_callback(packet):
    print(packet)

    packet.accept()


queue = NetfilterQueue()
queue.bind(0, pkt_filter_callback)

try:
        print 'Controller packet filtering mode'
        queue.run()

except KeyboardInterrupt:
        print 'Quitting packet filter' 
        queue.unbind()

        raise KeyboardInterrupt
