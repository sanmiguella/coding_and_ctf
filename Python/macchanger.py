#!/usr/bin/env python

# Import the required modules for this program to work
import subprocess, optparse, re

# To restore to original mac addr:
# root@kali:~/scripts# ethtool -P eth0

def getArguments():
    parser = optparse.OptionParser() # Simplifies acessing methods so we are able to use shorthand instead of typing everything in full

    # Arguments for the program:
    # -i : interface , -m : mac address , -h : help
    parser.add_option("-i", "--interface", dest="interface", help="Interface for mac address change")
    parser.add_option("-m", "--mac", dest="new_mac", help="New mac address") 

    (options, arguments) = parser.parse_args() 

    if not options.interface: # If user doesn't input an interface
        parser.error("Please specify an interface, use --help for more info.")

    elif not options.new_mac: # If user doesn't input a mac address
        parser.error("Please specifiy a mac address, use --help for more info.")

    return options # If user input both interface and mac address


# Function must be defined first here before calling it later
def changeMacAddress(interface, new_mac):
    print('[+] Changing mac address for ' + interface + ' to ' + new_mac + '\n') 

    subprocess.call(['ifconfig', interface, 'down']) # Brings interface down
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac]) # Changes MAC addr
    subprocess.call(['ifconfig', interface, 'up']) # Brings interface up
    subprocess.call(['ifconfig', interface]) # Shows the interface details

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])

    # Using regex filter on ifconfig_results because we are only interested in mac address
    match_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if match_result: # If there is a match
        return(match_result.group(0))

    else: # If there isn't a match
        print("[-] Could not read MAC address.")

options = getArguments() # Gets argument from user
current_mac = get_current_mac(options.interface) # Calls function to get the current mac address

'''
if current_mac: # If there is a value inside current_mac variable
    print("Current MAC = " + current_mac) # Print current mac address to the console
'''

# So that when there's no value: None, it will display as None
print("Current MAC = " + str(current_mac)) 

#changeMacAddress(options.interface, options.new_mac) # Changes mac address

