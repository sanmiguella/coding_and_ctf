# Flags for gcc
CFLAGS=-fno-stack-protector -no-pie -zexecstack

# Will be used for make clean later
binaries=ex1 

# Associate source code with corresponding binary name
ex1: ex1.c

# Make all will clean directory too
all: clean $(binaries)

.PHONY: clean

# Clean binary files as well as object files
clean:
	rm  -f $(binaries) *.o
