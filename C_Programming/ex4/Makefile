# Flags for gcc
CFLAGS=-Wall -g

# Will be used for make clean later
binaries=ex4

# Associate source code with corresponding binary name
ex4: ex4.c 

# Make all will clean directory too
all: clean $(binaries)

.PHONY: clean

# Clean binary files as well as object files
clean:
	rm  -f $(binaries) *.o
