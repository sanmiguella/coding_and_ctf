# Flags for gcc
CFLAGS=-Wall -g -fno-stack-protector -no-pie -zexecstack

# Will be used for make clean later
binaries=test 

# Associate source code with corresponding binary name
test: test.c

# Make all will clean directory too
all: clean $(binaries)

.PHONY: clean

# Clean binary files as well as object files
clean:
	rm  -f $(binaries) *.o
