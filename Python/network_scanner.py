#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
	# List down ARP fields
	scapy.ls(scapy.ARP())
	print "\n"	
	
	# List down Ethernet fields
	scapy.ls(scapy.Ether())
	print "\n"

	# Set the required destination IP field
	arp_request = scapy.ARP(pdst=ip)
	arp_request.show()

	# Set the required destination MAC field
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	broadcast.show()

	# To broadcast to the whole subnetwork: 192.168.218.1/24
	# Destination broadcast MAC address ff:ff:ff:ff:ff:ff
	arp_request_broadcast = broadcast / arp_request

	# srp - send and receive
	answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)	

	print str(answered.summary()) + "\n"

	#print str(unanswered.summary())
	print unanswered

scan("192.168.218.1/24")
