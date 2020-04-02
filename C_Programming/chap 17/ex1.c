#include <stdio.h>

int main() {
    int count; 
    count=1; 

    while(count<=3) {   // While loop will continue until count is greater than 3
        printf("Current value of count : %d\n",count);
        count++; // IF there isn't any increment, while loop will continue endlessly.
    }

    return(0);
}
