# Flags for gcc
CFLAGS=-Wall -g -fno-stack-protector -no-pie -zexecstack

# Will be used for make clean later
binaries=ex4 ex5 justify

# Associate source code with corresponding binary name
ex4: ex4.c  
ex5: ex5.c
justify: justify.c

# Make all will clean directory too
all: clean $(binaries)

.PHONY: clean

# Clean binary files as well as object files
clean:
	rm  -f $(binaries) *.o
