# Flags for gcc
CFLAGS=-Wall -g -fno-stack-protector -no-pie -zexecstack

# Will be used for make clean later
binaries=ex4 ex5 ex6 ex7 ex8 justify

# Associate source code with corresponding binary name
ex4: ex4.c  
ex5: ex5.c
ex6: ex6.c
ex7: ex7.c
ex8: ex8.c
justify: justify.c

# Make all will clean directory too
all: clean $(binaries)

.PHONY: clean

# Clean binary files as well as object files
clean:
	rm  -f $(binaries) *.o
