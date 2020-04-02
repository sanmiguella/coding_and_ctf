#include <stdio.h>

int main() {
    puts("Start typing.");
    puts("Press q then Enter to stop.");
    
    while(getchar() != 'q') // As long as character entered isnt q, program loops
        ;

    puts("\nThanks!");

    return(0);
}
