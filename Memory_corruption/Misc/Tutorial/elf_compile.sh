#!/bin/sh
EXE="c_shellcode"

if [ -f "$EXE" ]; then
    echo "[-]Removing $EXE.."
    rm -v $EXE
else
    echo "[!]$EXE not found.."
fi

FILE="test.c"
if [ -f "$FILE" ]; then
    echo "[+]Compiling $FILE to $EXE"
    gcc -zexecstack -fno-stack-protector -no-pie $FILE -o $EXE
else
    echo "[!]$FILE not found.."
fi 
