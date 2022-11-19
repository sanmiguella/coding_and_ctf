#!/usr/bin/env python3
from xml.dom import minidom
import argparse
import texttable

def parse_xml():
    try:
        xmlDoc = minidom.parse(xmlFile)
        hostTag = xmlDoc.getElementsByTagName('host')
        notFound = True
        foundCount = 0
     
        tableObj = texttable.Texttable(0)
        tableObj.set_cols_align(['l', 'l']) # Align left
        tableObj.set_cols_dtype(['t', 't']) # Data type text
        tableObj.add_row(['IP Address', 'Port(s) open']) # Table header

        if noBorder:
            # No borders
            tableObj.set_deco(tableObj.HEADER)

        for host in hostTag:
            addressTag = host.getElementsByTagName('address')[0]
            ipAddr = addressTag.getAttribute('addr')

            host_portList = list()
            portsTag = host.getElementsByTagName('port')

            for singlePort in portsTag:
                portNum = int(singlePort.getAttribute('portid'))
                portStatusTag = singlePort.getElementsByTagName('state')[0]
                portStatus = portStatusTag.getAttribute('state')

                # Only get open ports for a single host
                if portStatus == 'open':
                    host_portList.append(portNum)

            if len(host_portList) > 0:
                if args.any:
                    # https://thispointer.com/python-check-if-a-list-contains-all-the-elements-of-another-list/
                    listedPortsExistOnHost = any(port in host_portList for port in portList)
                else:
                    listedPortsExistOnHost = all(port in host_portList for port in portList)
                
                if listedPortsExistOnHost:
                    notFound = False
                    foundCount += 1
                    ports =  ', '.join(str(port) for port in host_portList)
                    tableObj.add_row([ipAddr, ports]) # Table data

        if notFound:
            print(f'[-] No results')
        else:
            ports = ', '.join(str(port) for port in portList)

            if args.any:
                print(f'Found a total of {foundCount} IP addresses that matches any of the port(s) : ({ports})')
            else:
                print(f'Found a total of {foundCount} IP addresses that matches all of the port(s) : ({ports})')

            print(tableObj.draw())
    
    except Exception as err:
        print(f'[!] {err}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get host from port(s)')
    parser.add_argument('-f', '--xmlfile', help='Nmap xml file to read data from', required=True)
    parser.add_argument('-p', '--ports', nargs='+', type=int,  help='Ports separated by space', required=True)
    parser.add_argument('-nb', default=False, action='store_true', help='No table borders.')
    
    parseOpt = parser.add_mutually_exclusive_group(required=True)
    parseOpt.add_argument('-any', action='store_true', help='Matches any of the port(s).')
    parseOpt.add_argument('-all', action='store_true', help='Matches all of the port(s).')

    args = parser.parse_args()
    xmlFile = args.xmlfile

    # https://realpython.com/python-sort/
    portList = sorted(args.ports)
    noError = True
    noBorder = args.nb

    for port in portList:
        if port < 1 or port > 65535:
            noError = False
            print('[-] Ports range 1-65535')
            break

    if noError:
        parse_xml()
