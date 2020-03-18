#include <stdio.h>

int main()
{
    char key;
    
    printf("Press a key on your keyboard : "); 
    key =  getchar(); // Get input from user

    printf("\nYou pressed the \"%c\" key.\n", key); // Tell user the key that was pressed
    printf("Its ASCII value in decimal is \"%d\".\n", key); // Ascii key in decimal format
    printf("Its ASCII value in hexadecimal is \"0x%x\".\n", key); // Ascii key in hexadecimal format

    return(0);
}
