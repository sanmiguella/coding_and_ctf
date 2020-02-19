#!/bin/sh

if [ -f "$1.c" ] ; then
    sudo rm -v $1
    echo "[+] $1 removed!"

    echo "[+] Compiling $1.c to $1"
    gcc -no-pie -fno-stack-protector -zexecstack vuln.c -o vuln

    echo "[+] Changing owner to root"
    sudo chown root:root $1

    echo "[+] Suid-ing binary"
    sudo chmod +s $1
else
    echo "[!] $1.c not found"
fi

