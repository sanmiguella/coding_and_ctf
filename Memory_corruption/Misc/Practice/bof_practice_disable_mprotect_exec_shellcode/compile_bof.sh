#!/bin/bash

FILE="bof"
if [ -f "$FILE" ] ; then
    echo "[+] Removing $FILE"
    rm -v bof
else
    echo "[-] $FILE not found!"
fi

echo "[+] Compiling bof.c to bof"
gcc -m32 -fno-stack-protector -no-pie bof.c -o bof
