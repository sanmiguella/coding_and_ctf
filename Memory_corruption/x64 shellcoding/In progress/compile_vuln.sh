#!/bin/sh
gcc -no-pie -fno-stack-protector -zexecstack vuln.c -o vuln
