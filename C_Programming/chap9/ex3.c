#include <stdio.h>
#include <string.h>

int main() 
{
    char greeting[] = "Hello\n";    // Declares an array of characters

    printf("Press enter...."); 
    getchar();                      // Get any character input and program will continue to the next instruction

    for(int i = 0; i < strlen(greeting); i++) {
        putchar(greeting[i]);       // Loops through every char in the array and print every char out to the console
    }

    return(0);
}
