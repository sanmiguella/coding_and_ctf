#!/bin/bash
# sudo ./enable_ASLR.sh
echo 2 | tee /proc/sys/kernel/randomize_va_space
