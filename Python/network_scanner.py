#!/usr/bin/env python

import scapy.all as scapy
import struct

def scan(ip):
	# List down ARP fields
	# scapy.ls(scapy.ARP())
	# print "\n"	
	
	# List down Ethernet fields
	# scapy.ls(scapy.Ether())
	# print "\n"

	# Set the required destination IP field
	arp_request = scapy.ARP(pdst=ip)
	# arp_request.show()

	# Set the required destination MAC field
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	# broadcast.show()

	# To broadcast to the whole subnetwork: 192.168.218.1/24
	# Destination broadcast MAC address ff:ff:ff:ff:ff:ff
	arp_request_broadcast = broadcast / arp_request

	# srp - send and receive
	# List - Arrays in python
	answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]	
	
	# Banner
	print "-----" * 10
	print "IP" + "\t" * 3 + "MAC"
	print "-----" * 10 

	clients_list = []

	for element in answered_list:	
		# Dictionary of IP and MAC address
		clients_dict = {"ip":element[1].psrc, "mac":element[1].hwsrc}

		# Adds dictionary into list
		clients_list.append(clients_dict)
		print  clients_dict["ip"] + "\t" * 2 + clients_dict["mac"]

	print "\n"
	print clients_list

	# print str(answered_list.summary()) + "\n"

	# print str(unanswered_list.summary())
	# print unanswered_list

scan("192.168.40.0/24")

