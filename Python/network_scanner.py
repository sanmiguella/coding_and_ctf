#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
	scapy.ls(scapy.ARP())
	print "\n"	
	
	scapy.ls(scapy.Ether())
	print "\n"

	arp_request = scapy.ARP(pdst=ip)
	arp_request.show()

	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	broadcast.show()

	arp_request_broadcast = broadcast / arp_request
	answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)	

	print str(answered.summary()) + "\n"

	#print str(unanswered.summary())
	print unanswered

scan("192.168.218.1/24")
