#include <stdio.h>

int main() {
    int temp; 
   
    printf("Whats the temperature outside in celcius? "); 
    scanf("%d", &temp); 

    if (temp<33  && temp>28) {
        printf("Perfect temperature to go outside!\n");
    } else {
        printf("Prolly should have stayed indoors..\n");
    }

    return(0);
}
