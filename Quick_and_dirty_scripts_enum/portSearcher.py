#!/usr/bin/env python3
from xml.dom import minidom
import argparse

def parse_xml():
    xmlDoc = minidom.parse(xmlFile)
    hostTag = xmlDoc.getElementsByTagName('host')
    notFound = True
  
    for host in hostTag:
        addressTag = host.getElementsByTagName('address')[0]
        ipAddr = addressTag.getAttribute('addr')

        host_portList = list()
        portsTag = host.getElementsByTagName('port')

        for singlePort in portsTag:
            portNum = int(singlePort.getAttribute('portid'))
            host_portList.append(portNum)

        if len(host_portList) > 0:
            # https://thispointer.com/python-check-if-a-list-contains-all-the-elements-of-another-list/
            listedPortsExistOnHost = all(port in host_portList for port in portList)
            
            if listedPortsExistOnHost:
                notFound = False
                ports =  ' '.join(str(port) for port in host_portList)
                print(f'[+] {portList} found on {ipAddr} - {ports}')

    if notFound:
        print(f'[-] {portList} not found on {xmlFile}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get host from port(s)')
    parser.add_argument('-f', '--xmlfile', help='Nmap xml file to read data from', required=True)
    parser.add_argument('-p', '--ports', nargs='+', type=int,  help='Ports separated by space', required=True)

    args = parser.parse_args()
    xmlFile = args.xmlfile
    portList = args.ports

    parse_xml()
