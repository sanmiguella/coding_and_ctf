#include <stdio.h>

void overflow(); // Function prototype

int main() {
    overflow(); // Calls overflow()
    return 0;     
}

void overflow() {
    char buf[256]; // Declares a buffer of 256 bytes

    printf("Input anything: "); 
    gets(buf); // Data will be stored in buf[], theres no boundary checking

    printf("You entered: %s\n", buf);
}
