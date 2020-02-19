#!/bin/sh
sudo rm -v shellcode
./compile.sh shellcode
sudo chown root:root shellcode
sudo chmod +s shellcode
