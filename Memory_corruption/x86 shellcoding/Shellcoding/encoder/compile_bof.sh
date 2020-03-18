#!/bin/bash
echo "[+] Removing bof"
rm -v bof

echo "[+] Compiling bof.c to bof"
gcc -m32 -fno-stack-protector -no-pie bof.c -o bof
