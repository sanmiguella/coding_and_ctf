#!/bin/bash

if [ -f $1.c ]; then
    if [ -f $1 ]; then
        echo "[-] Removing old $1"
        rm -v $1
    else
        echo "[!] Old $1 not found!"
    fi    

    echo "[+] Compiling $1.c to $1"
    gcc -fno-stack-protector -zexecstack -no-pie $1.c -o $1
else
    echo "[-] $1.c not found!"
fi
