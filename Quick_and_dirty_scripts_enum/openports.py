#!/usr/bin/env python3
from xml.dom import minidom
import argparse
import texttable

def parse_xml():
    try:
        xmlDoc = minidom.parse(xmlFile)
        hostTags = xmlDoc.getElementsByTagName('host')

        tableObj = texttable.Texttable(0)
        tableObj.set_cols_align(['l', 'l'])
        tableObj.set_cols_dtype(['t', 't'])
        tableObj.add_row(['IP Address', 'Open port(s)'])

        if noBorder:
            tableObj.set_deco(tableObj.HEADER)

        for hostTag in hostTags:
            addressTag = hostTag.getElementsByTagName('address')[0]
            ipAddr = addressTag.getAttribute('addr')

            singleHost_portList = list()
            portTags = hostTag.getElementsByTagName('port')

            for portTag in portTags:
                portNum = int(portTag.getAttribute('portid'))
                portStatusTag = portTag.getElementsByTagName('state')[0]
                portStatus = portStatusTag.getAttribute('state')

                if portStatus == 'open':
                    singleHost_portList.append(portNum)

            if len(singleHost_portList) > 0:
                ports = ', '.join(str(port) for port in singleHost_portList)
                tableObj.add_row([ipAddr, ports])

        print(tableObj.draw())

    except Exception as err:
        print(f'[!] {err}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get open port(s)')
    parser.add_argument('-f', '--xmlfile', help='Nmap xml file to read data from.', required=True)
    parser.add_argument('-nb', default=False, action='store_true', help='No table borders.')
    
    args = parser.parse_args()
    xmlFile = args.xmlfile
    noBorder = args.nb

    parse_xml()
