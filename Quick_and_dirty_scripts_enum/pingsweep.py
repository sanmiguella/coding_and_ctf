#!/usr/bin/env python3
# Improved the source code from https://rubysash.com/programming/python/python-3-multi-threaded-ping-sweep-scanner/
import ipaddress
import threading
import argparse

from time import time
from subprocess import Popen, PIPE
from queue import Queue

def saveResults():
    with open(args.output, 'w+') as f:
        for ip in foundList:
            f.write(f'{ip}\n')

def pingSweep(ip):
    ipAddress = str(allHosts[ip])
    output = Popen(['ping', '-c', '1', '-w', '150', ipAddress], stdout=PIPE).communicate()[0]

    # lock this section, until w get a complete chunk
    # then free it (so it doesn't write all over itself)
    with printLock:
        # code logic if we have/don't have good response
        if '64 bytes from' in output.decode('utf-8'): 
            if args.output:
                foundList.append(ipAddress)

            print(f'> {ipAddress} is Online.')

# defines a new ping using def pingSweep for each thread
# holds task until thread completes
def threader():
    while True:
        worker = q.get()
        pingSweep(worker)
        q.task_done()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ping sweeps utility for legacy IPv4 network.')
    parser.add_argument('-n', '--network', type=str, help='Target network address, eg. 192.168.2.0/24', required=True)
    parser.add_argument('-t', '--threads', type=int, nargs='?', const=32, default=32, help='Number of threads.')
    parser.add_argument('-o', '--output', type=str, help='Save results to file.')
    args = parser.parse_args()

    try:
        # Create the network
        ipNetwork = ipaddress.ip_network(args.network)

        # Get all hosts on that network
        allHosts = list(ipNetwork.hosts())

    except Exception as err:
        print(f'[-] {err}')

    else:
        printLock = threading.Lock()

        # Quick message/update
        print(f'[+] Sweeping {args.network} with {args.threads} threads')
        startTime = time()

        # To be used with args.output
        foundList = list()

        q = Queue()

        # up to 32 threads, daemon for cleaner shutdown
        # just spawns the threads and makes them daemon mode
        for x in range(args.threads):
            t = threading.Thread(target = threader)
            t.daemon = True
            t.start()

        # loops over the last octet in our network object
        # passing it to q.put (entering it into queue)
        for worker in range(len(allHosts)):
            q.put(worker)

        # queue management
        q.join()

        #ok, give us a final time report
        runtime = float('%0.2f' % (time() - startTime))
        print(f'[+] Run Time: {runtime} seconds')

        if args.output:
            saveResults()
