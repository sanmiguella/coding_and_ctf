#include <stdio.h>

int main()
{
    char menu_item[] = "Slimy orange stuff\"Icky woka gu\"";  // Backslash escape strings for double quote
    int pints = 1; 
    float price = 1.45; 

    printf("Today's special - %s\n", menu_item); 
    printf("You want %d pint.\n", pints); 
    printf("That be $%.2f, please.\n", price);                // 2 decimal places for floating point values

    return(0);
}
