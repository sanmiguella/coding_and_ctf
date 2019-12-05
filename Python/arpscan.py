#!/usr/bin/env python

# So we won't need to type scapy.all
import scapy.all as scapy

def scan(ip):
	# pdst :IPField -> Destination
	# ARP who has Net('192.168.218.1/24') says 192.168.218.163
	arp_request = scapy.ARP(pdst=ip)

	print(arp_request.summary()) + "\n"

	# Listing of various fields which could be customized
	#scapy.ls(scapy.ARP())
	
scan("192.168.218.1/24")
