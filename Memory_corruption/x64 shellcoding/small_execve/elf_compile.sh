#!/bin/sh
EXE="c_shellcode"

if [ -f "$EXE" ]; then
    echo "[-]Removing $EXE.."
    sudo rm -v $EXE
else
    echo "[!]$EXE not found.."
fi

FILE="test.c"
if [ -f "$FILE" ]; then
    echo "[+]Compiling $FILE to $EXE"
    gcc -zexecstack -fno-stack-protector -no-pie $FILE -o $EXE

    sudo chown root:root $EXE
    sudo chmod +s $EXE
else
    echo "[!]$FILE not found.."
fi 
