#!/usr/bin/env/python

import os
import optparse
import subprocess
import argparse


# import pyfiglet

def strings_check(filename, flag2grep):
        print("\033[1;32;10m [+] Strings checking " + filename + " grep: " + flag2grep + "\n")
        print("\033[0;37;10m     ... \n")
        # ascii_banner = pyfiglet.figlet_format("I hate it")
        # print(ascii_banner)
        os.system("strings " + filename + " | grep " + flag2grep)
        print("\033[1;32;10m [+] Strings done \n")


def foremost_check(filename):
        print("\033[1;32;10m [+] Trying to extract everything with foremost from " + filename + "\n")
        print("\033[0;37;10m     ... \n")
        subprocess.call(["foremost", "-T", filename])
        print("\033[1;32;10m [+] Foremost done \n [+] Check output folder, please \n")


def binwalk_check(filename):
        print("\033[1;32;10m [+] Trying to extract everything with binwalk from " + filename + "\n")
        print("\033[0;37;10m     ... \n")
        subprocess.call(["binwalk", "-e", filename])
        print("\033[1;32;10m [+] Binwalk done \n [+] Check output folder, please \n")


def get_arguments():
        parser = optparse.OptionParser()
        parser.add_option("-f", "--filename", dest="filename", help="Name of the file to check")
        parser.add_option("-F", "--flag2grep", dest="flag2grep", help="Word or command to use with grep")
        parser.add_option("-b", "--binwalk", dest="binwalk", action="store_true", help="Use binwalk")
        parser.add_option("-o", "--foremost", dest="foremost", action="store_true", help="Use foremost")
        parser.add_option("-s", "--strings", dest="strings", action="store_true", help="Use strings with grep")
        return parser.parse_args()


(options, arguments) = get_arguments()
if options.binwalk:
        binwalk_check(options.filename)
if options.foremost:
        foremost_check(options.filename)
if options.strings:
        strings_check(options.filename, options.flag2grep)
else:
        binwalk_check(options.filename)
        foremost_check(options.filename)
        strings_check(options.filename, options.flag2grep)
