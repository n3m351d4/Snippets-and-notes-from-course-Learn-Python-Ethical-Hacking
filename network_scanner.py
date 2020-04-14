#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    # list clients of the network and MAC addresses
    # scapy.arping(ip) can take IP ranges
    arp_request = scapy.ARP(pdst=ip)
    # arp_request.show()
    # print(arp_request.summary())
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # set destination MAC to broadcast
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    # send packets combined of parts and receive response, answered_list and unanswered_list
    print("__________________________________________\nIP\t\t\tMAC Address\n------------------------------------------")
    for element in answered_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
        # parse the values


scan("192.168.1.254/24")
# 192.168.1.77/24 my IP
