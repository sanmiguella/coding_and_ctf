#!/bin/sh 

FILE="$1"
if [ -f "$FILE" ]; then
    echo "[+] Removing $FILE"
    rm -v $FILE
else
    echo "[!] $FILE not found!"
fi

FILE="$1.o"
if [ -f "$FILE" ]; then 
    echo "[+] Removing $FILE"
    rm -v $FILE
else
    echo "[!] $FILE not found!"
fi

FILE="$1.asm"
if [ -f "$FILE" ]; then
    echo "[+] Compiling source to object file -> $1.o"
    nasm -f elf64 $1.asm -o $1.o
    echo "[+] Linking object file to executable -> $1"
    ld -m elf_x86_64 $1.o -o  $1
else 
    echo "[!] $FILE not found!"
fi
