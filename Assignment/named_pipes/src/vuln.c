/* This program has a buffer overflow vulnerability. */
/* Our task is to exploit this vulnerability */
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

unsigned int xormask = 0xBE;
int i, length;

int bof(FILE *badfile)
{
    char buffer[12];

    /* The following statement has a buffer overflow problem */
    length = fread(buffer, sizeof(char), 52, badfile);

    /* XOR the buffer with a bit mask */
    for (i=0; i<length; i++) {
        buffer[i] ^= xormask;
    }

    return 1;
}

int main(int argc, char **argv)
{
    FILE *badfile;

    badfile = fopen("badfile", "r");
    bof(badfile);

    printf("Returned Properly\n");

    fclose(badfile);

    return 1;
}

