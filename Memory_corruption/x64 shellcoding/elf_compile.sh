#!/bin/sh
FILE="test"

if [ -f "$FILE" ]; then
    echo "[-]Removing $FILE.."
else
    echo "[!]$FILE not found.."
fi

FILE="test.c"
if [ -f "$FILE" ]; then
    echo "[+]Compiling $FILE to test"
    gcc -zexecstack -fno-stack-protector -no-pie $FILE -o test
else
    echo "[!]$FILE not found.."
fi 
