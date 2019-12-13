#!/usr/bin/env python

import scapy.all as scapy
import optparse

def getArguments():
	parser = optparse.OptionParser()

	# Arguments for the progra:
	#	-i : subnetwork ip address
	#	-m : subnet mask
	parser.add_option("-i", "--ip", dest="ip_addr", help="Subnetwork ip address")
	parser.add_option("-m", "--mask", dest="mask", help="Subnet mask")

	(options, arguments) = parser.parse_args()

	if not options.ip_addr: # If user doesn't specify ip address
		parser.error("Please specify an ip address, use --help for more info")
	elif not options.mask: # If user doesn't specify subnet mask
		parser.error("Please specify subnet mask, use --help for more info")
	
	# Returns both the ip address and subnet mask to the calling variable
	return options 


def scan(ip):
	# Set the required destination IP field
	arp_request = scapy.ARP(pdst=ip)

	# Set the required destination MAC field
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

	# To broadcast to the whole subnetwork: 192.168.218.1/24
	# Destination broadcast MAC address ff:ff:ff:ff:ff:ff
	arp_request_broadcast = broadcast / arp_request

	# srp - send and receive
	# List - Arrays in python
	answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]	
	
	clients_list = []

	for element in answered_list:	
		# Dictionary of IP and MAC address
		clients_dict = {"ip":element[1].psrc, "mac":element[1].hwsrc}

		# Adds dictionary into list
		clients_list.append(clients_dict)

	return clients_list


def print_result(results_list):
	# Banner
	print "-----" * 10
	print "IP" + "\t" * 3 + "MAC"
	print "-----" * 10 

	# Prints every client in results list
	for client in results_list:
		print  client["ip"] + "\t" * 2 + client["mac"]


options = getArguments() # Get argument
ip = options.ip_addr + "/" + options.mask # Form argument to be passed to scan()
scan_results = scan(ip) # Scans the network
print_result(scan_results) # Print result to user in readable form

