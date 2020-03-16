# Flags for gcc
CFLAGS=-Wall -g -fno-stack-protector -no-pie -zexecstack

# Will be used for make clean later
binaries=ex1 ex2 ex3 ex4 test

# Associate source code with corresponding binary name
ex1: ex1.c
ex2: ex2.c
ex3: ex3.c
ex4: ex4.c
test: test.c

# Make all will clean directory too
all: clean $(binaries)

.PHONY: clean

# Clean binary files as well as object files
clean:
	rm  -f $(binaries) *.o
