#!/bin/bash
gcc -m32 -no-pie -zexecstack -fno-stack-protector bo.c -o bo
