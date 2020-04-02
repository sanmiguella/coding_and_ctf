#include <stdio.h>

int main() {
    char input; 

    puts("Start typing...");
    puts("Press ~ then Enter to stop");

    for(;;) {
        input = getchar();

        if(input == '~') {
            break; 
        } 
    }

    puts("Thanks!");
    return(0);
}
