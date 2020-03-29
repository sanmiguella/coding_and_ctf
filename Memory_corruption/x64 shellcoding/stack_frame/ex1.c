#include <stdio.h>
#define BUF_SIZE 1024

void proc() {
    char buffer[BUF_SIZE];
    printf("Hello world!\n");
}

int main() {
    char buffer[BUF_SIZE];
    proc();
    return(0); 
}
