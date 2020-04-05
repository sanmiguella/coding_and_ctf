#include <stdio.h>

int main() {
    int count;
    char output;

    printf("Nested loops..\n\n");

    for(count=1;count<=3;count++) {
        for(output='A';output<='C';output++) {
            printf("Loop(%d) -> %c ", count, output); 
        }

        putchar('\n');  // newline
    }

    puts("\nAnd we are done!!");
    return(0);
}
