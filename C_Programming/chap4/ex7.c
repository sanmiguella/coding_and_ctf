#include <stdio.h>
#define BUF_SIZE 32

int main() {  
    // Declare variables with a small buffer size 
    char adjective[BUF_SIZE], food[BUF_SIZE], chore[BUF_SIZE], furniture[BUF_SIZE]; 
   
    //  Getting user input 
    printf("Enter an adjective -> "); 
    scanf("%s", adjective); 

    printf("Enter a food -> "); 
    scanf("%s", food); 

    printf("Enter a household chore -> "); 
    scanf("%s", chore); 

    printf("Enter an item of furniture -> "); 
    scanf("%s", furniture); 

    // Displaying custom message using earlier input  
    printf("\n\nDon't touch that %s %s!\n", adjective, food); 
    printf("I just %s the %s!\n", chore, furniture); 

    return(0);
}
