#!/usr/bin/python3
from xml.dom import minidom
import argparse
import texttable

ipv4_dict = dict()
ipv6_dict = dict()
ipv4_to_ipv6_dict = dict()

def readXML(filename, ip_type):
    # https://stackoverflow.com/questions/69320197/write-nmap-xml-scans-in-a-file-and-compare-them
    xmldoc = minidom.parse(filename)
    hosts = xmldoc.getElementsByTagName('hosthint')

    for host in hosts:
        address = host.getElementsByTagName('address')
        ip_addr = address[0].attributes["addr"].value
        mac_addr = address[1].attributes["addr"].value

        if ip_type == "ipv4":
            ipv4_dict[mac_addr] = ip_addr
        elif ip_type == "ipv6":
            ipv6_dict[mac_addr] = ip_addr

def compare():
    ipv4_temp_dict = dict()
    ipv6_temp_dict = dict()

    # Get dual stack IPv4 and IPv6. For IPv4 address without any corresponding IPv6 address, add them 
    for mac_addr in ipv4_dict:
        ipv4_addr = ipv4_dict[mac_addr]
    
        # https://thispointer.com/python-check-if-a-value-exists-in-the-dictionary-3-ways/
        if mac_addr in ipv6_dict.keys():
            # https://www.pythonforbeginners.com/dictionary/get-key-from-value-in-dictionary
            ipv6_dict_items = ipv6_dict.items()

            for ipv6_mac_addr, ipv6_addr in ipv6_dict_items:
                if ipv6_mac_addr == mac_addr:
                    ipv4_to_ipv6_dict[mac_addr] = [ipv4_addr, ipv6_addr]
                    break
        else:
            ipv4_temp_dict[mac_addr] = [ipv4_addr, "None"]

    for mac_addr in ipv6_dict:
        ipv6_addr = ipv6_dict[mac_addr]
    
        if mac_addr in ipv4_dict.keys():
            pass
        else:
            ipv6_temp_dict[mac_addr] = ["None", ipv6_addr]    

    # Adds the remaining only IPv6 address to ipv4_to_ipv6_dict
    for mac_addr in ipv6_temp_dict:
        ipv4_to_ipv6_dict[mac_addr] = ipv6_temp_dict[mac_addr]

    # Adds the remaining only IPv4 address to ipv4_to_ipv6_dict
    for mac_addr in ipv4_temp_dict:
        ipv4_to_ipv6_dict[mac_addr] = ipv4_temp_dict[mac_addr]

def show_output():
    # https://www.geeksforgeeks.org/texttable-module-in-python/
    tableObj = texttable.Texttable(0)
    tableObj.set_cols_align(["l", "l", "l"])
    tableObj.set_cols_dtype(["t", "t", "t"])

    tableObj.add_row(["Mac Address", "Legacy IP", "IPv6"])
    for mac_addr in ipv4_to_ipv6_dict:
        ipv4_addr = ipv4_to_ipv6_dict[mac_addr][0]
        ipv6_addr = ipv4_to_ipv6_dict[mac_addr][1]
        tableObj.add_row([mac_addr, ipv4_addr, ipv6_addr])

    print(tableObj.draw())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compares IPv4 and IPv6 nmap.xml file.")
    parser.add_argument("-4", "--v4", help="IPv4 nmap xml file.", required=True)
    parser.add_argument("-6", "--v6", help="IPv6 nmap xml file.", required=True)
    args = parser.parse_args()

    ipv4_xmlFile = args.v4 
    ipv6_xmlFile = args.v6

    readXML(ipv4_xmlFile, "ipv4")
    readXML(ipv6_xmlFile, "ipv6")

    compare()
    show_output()