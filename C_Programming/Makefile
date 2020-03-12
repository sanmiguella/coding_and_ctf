# Flags for gcc
CFLAGS=-Wall -g

# Will be used for make clean later
binaries=print print2

# Associate source code with corresponding binary name
print: print.c
print2: print2.c

# Make all will clean directory too
all: clean $(binaries)

.PHONY: clean

# Clean binary files as well as object files
clean:
	rm  -f $(binaries) *.o
