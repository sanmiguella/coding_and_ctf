#!/usr/bin/python3
import argparse
import socket

ipv4_list = []

def read_from_file(file_to_read):
    with open(file_to_read,'r') as f:
        hostnames = f.readlines()

    return(hostnames)

def save_ipv4_list(filename):
    # Sort and save ipv4s in the list to a file
    ipv4_list.sort()

    with open(filename,'w') as ipv4_file:
        for ipv4 in ipv4_list:
            ipv4_file.write(f"{ipv4}\n")

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Get IPv4 from hostname")
    parser.add_argument("file_to_read", help="Enter file containing a list of hostnames")

    args = parser.parse_args()
    hostnames = read_from_file(args.file_to_read.strip())

    # Check hostname 1 by 1
    for index, hostname in enumerate(hostnames):
        hostname = f"{hostname.strip()}"

        try:
            print(f"\n[{index}] ---> Resolving \"{hostname}\" <---\n")
            ipv4 = socket.gethostbyname(hostname)
            ipv4_list.append(ipv4)
            print(f"Ipv4 : {ipv4}")

        except Exception as err:
            print(f"Error -> {err}")

    save_ipv4_list("./ipv4_list.txt")
