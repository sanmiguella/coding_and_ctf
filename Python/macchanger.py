#!/usr/bin/env python 
import subprocess
import optparse

parser = optparse.OptionParser() # To simplify accessing method()

# Command switch as well as displaying help in case user types -> python maccchanger.py -h
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="newMac", help="New mac address")

(options, arguments) = parser.parse_args()

# Value of -i, -m are contained inside options properties(values/variables)
# Methods = functions()
# Properties = variables
interface = options.interface
newMac = options.newMac

print("[+] Changing mac address for interface " + interface + " to " + newMac + "\n")

# Every command is a separate string
subprocess.call(["ifconfig", interface, "down"]) # Brings interface down 
subprocess.call(["ifconfig", interface, "hw", "ether", newMac]) # Change interface mac address to new address
subprocess.call(["ifconfig", interface, "up"]) # Brings interface up
subprocess.call(["ifconfig", interface]) # Shows user the interface values
