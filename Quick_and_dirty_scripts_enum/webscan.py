#!/usr/bin/env python3
# Improved the source code from https://rubysash.com/programming/python/python-3-multi-threaded-ping-sweep-scanner/
import threading
import argparse

from time import time
from subprocess import Popen, PIPE
from queue import Queue

def webScan(host):
    outfile = f'nikto-{host}_.txt'
    output = Popen(['/usr/bin/nikto', '-host', host, '-port', '443', '-Tuning', 'x6', '-Format', 'txt', '-output', outfile], stdout=PIPE).communicate()[0]

    # lock this section, until w get a complete chunk
    # then free it (so it doesn't write all over itself)
    with printLock:
        print(output.decode())

# defines a new webscan using def webScan for each thread
# holds task until thread completes
def threader():
    while True:
        worker = q.get()
        webScan(worker)
        q.task_done()

def readFromFile(filename):
    with open(filename, 'r') as f:
        data = [line.strip() for line in f.readlines()]

    return data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Running webscan in parallel.')
    parser.add_argument('-f', '--hostfile', type=str, help='Read host list from file', required=True)
    args = parser.parse_args()
    threadNum = 32

    try:
        # Read hosts from file
        hostList = readFromFile(args.hostfile)
        #print(hostList)

    except Exception as err:
        print(f'[-] {err}')

    else:
        printLock = threading.Lock()

        # Quick message/update
        print(f'[+] Starting nikto scan...')
        startTime = time()

        q = Queue()

        # up to 32 threads, daemon for cleaner shutdown
        # just spawns the threads and makes them daemon mode
        for x in range(threadNum):
            t = threading.Thread(target=threader)
            t.daemon = True
            t.start()

        # loops over the last octet in our network object
        # passing it to q.put (entering it into queue)
        for worker in hostList:
            q.put(worker)

        # queue management
        q.join()

        # Ok, give us a final time report
        runtime = float('%0.2f' % (time() - startTime))
        print(f'[+] Run Time: {runtime} seconds')
