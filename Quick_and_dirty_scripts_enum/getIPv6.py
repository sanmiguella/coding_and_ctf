#!/usr/bin/python3
import argparse
import socket

ipv6_list = []

def read_from_file(file_to_read):
    with open(file_to_read,'r') as f:
        hostnames = f.readlines()

    return(hostnames)

def save_ipv6_list(filename):
    # Sort and save ipv6s in the list to a file
    ipv6_list.sort()

    with open(filename,'w') as ipv6_file:
        for ipv6 in ipv6_list:
            ipv6_file.write(f"{ipv6}\n")

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Get IPv6 from hostname")
    parser.add_argument("file_to_read", help="Enter file containing a list of hostnames")

    args = parser.parse_args()
    hostnames = read_from_file(args.file_to_read.strip())

    # Check hostname 1 by 1
    for index, hostname in enumerate(hostnames):
        hostname = f"{hostname.strip()}"

        try:
            print(f"\n[{index}] ---> Resolving \"{hostname}\" <---\n")
            result = socket.getaddrinfo(hostname, 443, socket.AF_INET6)
            ipv6 = result[0][4][0]
            ipv6_list.append(f"{hostname} {ipv6}")
            print(f"IPv6 : {ipv6}")

        except Exception as err:
            print(f"Error -> {err}")

    save_ipv6_list("./ipv6_list.txt")
