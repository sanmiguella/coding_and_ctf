#!/usr/bin/env python3
from xml.dom import minidom
import argparse
import texttable

def parseXML(fname):
    global totalHostCount
    global totalPortCount

    # Reference: https://mkyong.com/python/python-read-xml-file-dom-example/
    doc = minidom.parse(fname)
    hostTag = doc.getElementsByTagName('host')

    portsFound = False

    for ht in hostTag:
        addressTag = ht.getElementsByTagName('address')[0]
        hostnamesTag = ht.getElementsByTagName('hostnames')
        portsTag = ht.getElementsByTagName('port')

        ipAddr = addressTag.getAttribute('addr')

        hostname = 'None'
        try:
            for h in hostnamesTag:
                hostnameTag = h.getElementsByTagName('hostname')[0]
                hostname = hostnameTag.getAttribute('name')
        except:
            pass

        portsPerHostCount = 0
        try:
            for p in portsTag:
                #portID = p.getAttribute('portid')
                portsPerHostCount += 1
                totalPortCount += 1
                portsFound = True

            # Host count will only get incremented if the total number of port > 0.
            if portsFound:
                totalHostCount += 1
                portsFound = False
        except:
            pass

        # Only add entries if ports per host > 0
        if portsPerHostCount > 0:
            tableObj.add_row([ipAddr, hostname, portsPerHostCount])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get total number of hosts and services from Nmap xml file(s).")
    parser.add_argument("-f", "--xmlFile", type=argparse.FileType('r'), help="One or more Nmap xml file(s) to read data from.", nargs='+', required=True)
    args = parser.parse_args()

    fnames = args.xmlFile

    tableObj = texttable.Texttable(0)
    tableObj.set_cols_align(["l", "l", "l"])
    tableObj.set_cols_dtype(["t", "t", "t"])
    tableObj.set_deco(tableObj.HEADER) # Comment out to include borders.
    tableObj.add_row(['IP Address', 'Hostname', 'Num of Port(s)'])

    totalHostCount = 0
    totalPortCount = 0
    for f in fnames: parseXML(f)

    print(tableObj.draw()) 
    print(f'\nTotal host(s): {totalHostCount}\nTotal port(s): {totalPortCount}')
