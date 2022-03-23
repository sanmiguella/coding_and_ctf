#!/usr/bin/python3
from argparse import ArgumentParser
from texttable import Texttable
from concurrent.futures import ThreadPoolExecutor
import nmap

def read_from_file(filename):
    with open(filename, 'r') as f:
        hostnames = f.readlines()
    
    return(hostnames)

def scan(target, scan_type):
    try:
        nm = nmap.PortScanner()

        if scan_type == "4":
            nm.scan(target, arguments='-sT')
        elif scan_type == "6":
            nm.scan(target, arguments='-6 -sT')

        for host in nm.all_hosts():
            print(f"\n{host} ({nm[host].hostname()})")

            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()

                data_obj = Texttable(0)
                data_obj.set_cols_align(["l", "l", "l"])
                data_obj.set_cols_dtype(["t", "t", "t"])
                data_obj.add_row(["Port Number", "State", "Protocol"])

                for port in lport:
                    data_obj.add_row([port, nm[host][proto][port]['state'], proto])

                print(data_obj.draw())
    
    except Exception as err:
        print(f'[!] {err}')

if __name__ == "__main__":
    parser = ArgumentParser(description='Scan web servers using python3 nmap library.')
    parser.add_argument("-t", "--target", help="Target to scan.")
    parser.add_argument("-i", "--ifile", help="File containing list of hosts.")
    parser.add_argument("-6", "--v6", help="Set this to 6 for IPv6 portscan, else it will default to IPv4.")
    args = parser.parse_args()

    target = args.target
    inputfile = args.ifile
    v6 = args.v6

    if v6 != "6":
        v6 = "4"

    if target:
        scan(target, v6)
    elif inputfile:
        hostnames = read_from_file(inputfile)
   
        with ThreadPoolExecutor(max_workers=20) as executor:
            for hostname in hostnames:
                executor.submit(scan, hostname, v6)
    else:
        parser.print_help()
