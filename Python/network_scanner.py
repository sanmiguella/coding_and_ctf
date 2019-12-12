#!/usr/bin/env python

import scapy.all as scapy
import struct

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

	for client in results_list:
		#print(client)
		print  client["ip"] + "\t" * 2 + client["mac"]


scan_results = scan("192.168.2.0/24")
print_result(scan_results)


