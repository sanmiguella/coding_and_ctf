#include <stdio.h>
#include <stdlib.h>
#define BUF_SIZE 4

int main()
{
    char weight[BUF_SIZE]; 
    int w; 
    
    printf("Enter your weight -> "); 
    gets(weight); 
    w = atoi(weight);   // Convert from string to integer

    printf("Here is what you weigh now: %d\n", w);
    
    w += 1;
    printf("\nYour weight after the potatoes: %d\n", w);
    
    w += 1;
    printf("Here you are after the mutton: %d\n", w);
    
    w += 8;
    printf("And your weight aftert dessert: %d pounds!\n", w);
    
    printf("\nLardo!\n");
    return(0); 
}
