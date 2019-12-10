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
	answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]	

	for element in answered_list:	
		print "\n" + "=====" * 10
		print "Reply from"
		print "=====" * 10
		print "IP  ~ " + element[1].psrc 
		print "MAC ~ " + element[1].hwsrc
		print "=====" * 10
	print "\n"

	# print str(answered_list.summary()) + "\n"

	# print str(unanswered_list.summary())
	# print unanswered_list

scan("192.168.40.0/24")

