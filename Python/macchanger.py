#!/usr/bin/env python

# Import the required modules for this program to work
import subprocess
import optparse

# To restore to original mac addr:
# root@kali:~/scripts# ethtool -P eth0

# Function must be defined first here before calling it later
def changeMacAddress(interface, new_mac):
    print('[+] Changing mac address for ' + interface + ' to ' + new_mac + '\n') 

    subprocess.call(['ifconfig', interface, 'down']) # Brings interface down
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac]) # Changes MAC addr
    subprocess.call(['ifconfig', interface, 'up']) # Brings interface up
    subprocess.call(['ifconfig', interface]) # Shows the interface details


parser = optparse.OptionParser() # Simplifies acessing methods so we are able to use shorthand instead of typing everything in full

# Arguments for the program:
# -i : interface , -m : mac address , -h : help
parser.add_option("-i", "--interface", dest="interface", help="Interface for mac address change")
parser.add_option("-m", "--mac", dest="new_mac", help="New mac address") 

(options, arguments) = parser.parse_args()

# Calls the changeMacAddress() function
changeMacAddress(options.interface, options.new_mac)

