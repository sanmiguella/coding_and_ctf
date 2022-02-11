#!/usr/bin/python3
import socket
import re

if __name__ == "__main__":
    ipv4 = ''
    ipv6 = ''

    with open("./valid.txt", 'r') as valid_file:
        urls = valid_file.readlines()

    for url in urls:
        try:
            hostname = re.sub(r'https://|\n', "", url)
        
            ipv4 = socket.gethostbyname(hostname)
            ipv6 = socket.getaddrinfo(hostname, 443, socket.AF_INET6)
            ipv6 = ipv6[0][4][0]
            #results = socket.getaddrinfo(hostname, 443)

        except Exception as err:
            ipv6 = 'No ipv6'

        finally:     
            print(f"{hostname} -> {ipv4} (ipv4) , {ipv6} (ipv6)")
