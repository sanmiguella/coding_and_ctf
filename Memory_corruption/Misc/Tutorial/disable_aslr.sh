#!/bin/bash
ASLR="/proc/sys/kernel/randomize_va_space"

if [ -f $ASLR ] ; then
    echo "[+] Disabling ASLR"
    echo 0 | sudo tee -a $ASLR
else
    echo "[-] $ASLR not found!"
fi
