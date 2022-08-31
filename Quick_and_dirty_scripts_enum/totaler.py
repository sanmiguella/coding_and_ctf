#!/usr/bin/env python3
from xml.dom import minidom
import argparse
import texttable

def parseXML():
    # Reference: https://mkyong.com/python/python-read-xml-file-dom-example/
    doc = minidom.parse(fname)
    hostTag = doc.getElementsByTagName('host')

    tableObj = texttable.Texttable(0)
    tableObj.set_cols_align(["l", "l", "l"])
    tableObj.set_cols_dtype(["t", "t", "t"])
    tableObj.set_deco(tableObj.HEADER)
    tableObj.add_row(['IP Address', 'Hostname', 'Ports'])

    hostCount = 0
    portCount = 0

    for i, ht in enumerate(hostTag):
        addressTag = ht.getElementsByTagName('address')
        hostnamesTag = ht.getElementsByTagName('hostnames')
        portsTag = ht.getElementsByTagName('port')

        for i, a in enumerate(addressTag, 1):
            ipAddr = a.getAttribute('addr')
            hostCount += 1

        for h in hostnamesTag:
            hostnameTag = h.getElementsByTagName('hostname')[0]
            hostname = hostnameTag.getAttribute('name')

        ports = ''
        for i, p in enumerate(portsTag, 1):
            portID = p.getAttribute('portid')
            ports += f'{portID} '
            portCount += 1

        ports = ports.strip().replace(' ', ', ')
        tableObj.add_row([ipAddr, hostname, ports])

    print(tableObj.draw()) 
    print(f'\nTotal host(s): {hostCount}\nTotal port(s): {portCount}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get total number of hosts and services from nmap xml file.")
    parser.add_argument("-f", "--xmlFile", help="Nmap xml file to read data from.", required=True)
    args = parser.parse_args()

    fname = args.xmlFile
    parseXML()
