import sys

buf = ''
arg = sys.argv
filename = arg[1]

with open(filename,'r') as f:
    buf += f.read()

print "[+] File: " + filename
print "[+] Length: " + str(len(buf))
print "[!] Data: "
print buf