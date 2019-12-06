#!/usr/bin/env python

# So we won't need to type scapy.all
import scapy.all as scapy

def scan(ip):	
	'''
	###[ ARP ]### 
	  hwtype    = 0x1
	  ptype     = 0x800
	  hwlen     = 6
	  plen      = 4
	  op        = who-has
	  hwsrc     = 00:0c:29:ef:10:a7
	  psrc      = 192.168.40.149
	  hwdst     = 00:00:00:00:00:00
	  pdst      = Net('192.168.40.1/24')
	'''
	arp_request = scapy.ARP(pdst=ip) 
	arp_request.show()
	separate()

	'''
	###[ Ethernet ]### 
	  dst       = ff:ff:ff:ff:ff:ff
	  src       = 00:0c:29:ef:10:a7
	  type      = 0x9000
	'''
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") 
	broadcast.show()
	separate()
	
	'''
	###[ Ethernet ]### 
	  dst       = ff:ff:ff:ff:ff:ff
	  src       = 00:0c:29:ef:10:a7
	  type      = 0x806
	###[ ARP ]### 
	     hwtype    = 0x1
	     ptype     = 0x800
	     hwlen     = 6
	     plen      = 4
	     op        = who-has
	     hwsrc     = 00:0c:29:ef:10:a7
	     psrc      = 192.168.40.149
	     hwdst     = 00:00:00:00:00:00
	     pdst      = Net('192.168.40.1/24')
	'''
	arp_request_broadcast = broadcast/arp_request
	arp_request_broadcast.show()

	# print(arp_request.summary())
	# print(broadcast.summary())

	# Listing of various fields which could be customized
	# scapy.ls(scapy.ARP())
	# scapy.ls(scapy.Ether())	

def separate():
	print "=" * 50 + "\n"

scan("192.168.40.1/24")
