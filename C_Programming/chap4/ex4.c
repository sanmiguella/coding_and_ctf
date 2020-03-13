#include <stdio.h>

int main()
{
    char name[20];                                  // Set aside memory for input
    
    printf("What is your name? ");                  // Prompt
    scanf("%s", name);                              // Read input from keyboard and store it on computer memory
    printf("Darn glad to meet you, %s!\n", name);   // Prints a customized message using the input earlier
      
    return(0);
}
