#include <stdio.h>

int main() {
    int count;

    for(count=0; count<10; count+=2) {
        printf("Current value: %d\n", count);
    }

    return(0);
}
