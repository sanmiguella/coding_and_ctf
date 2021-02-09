#!/usr/bin/python3
import tftpy

ip = '192.168.56.106' # Remote host
port = 1337 # Remote port

with open("file.txt") as f:
    lines = f.readlines() # Read all string and store them in a list.

    client = tftpy.TftpClient(ip, port) # Connect to remote tftp server.

    for count, line in enumerate(lines):
        line = line.strip() # By default strings contain "\n" so we need to remove it.
        print(f"\nTrying {count} - {line}")

        # Try to download file, if encounter error, do nothing.
        try:
            client.download(line, line, timeout=5)
            print()
        except:
            pass