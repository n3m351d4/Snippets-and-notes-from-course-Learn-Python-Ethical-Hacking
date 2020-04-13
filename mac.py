#!/usr/bin/env python

import subprocess
# OS commands
import optparse
# user input commands


parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
(options, arguments) = parser.parse_args()
# capture arguments and options from user input, "-i" - option, "interface" - argument
# options then arguments, contains user input options.new_mac

# ctrl+d duplicate string
# ctrl+/ comment string

# variables:
# interface = "eth0"
# new_mac = "00:00:00:00:00:00"

# variables for input - options

interface = options.interface
new_mac = options.new_mac

# user input:
# interface = input("interface > ")
# new_mac = input("new MAC > ")
# for python2.7 raw_input("")

print("[+] Changing MAC address for " + interface + " to " + new_mac)

# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)
# not checking user input, just string, payload: ifconfig; ls; down (;ls;)
# to execute side commands!

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

# handling user input commands,anti-hijacking

# default: 
# experimental: de:ad:be:ef:ca:fe
