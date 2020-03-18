#include <stdio.h>
#include <string.h>

int main() 
{
    char greeting[] = "Hello\n";           // Declares an array of characters
    int count;
    int max_count = strlen(greeting);

    printf("Press enter...."); 
    getchar();                            // Get any character input and program will continue to the next instruction

    for(count = 0; count < max_count; count++) {
        char msg = greeting[count];
        putchar(msg);                     // Loops through every char in the array and print every char out to the console
    }

    return(0);
}
