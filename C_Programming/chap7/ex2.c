#include <stdio.h>
#include <stdlib.h>
#define BUF_SIZE 8
#define VAMPIRE_METHUSELAH 969

int main()
{
    int difference, age; 
    char years[BUF_SIZE]; 

    printf("How old are you? "); 
    gets(years); 
    age = atoi(years);  // Converts string to integer and assign it to an integer variable 
    
    difference = VAMPIRE_METHUSELAH - age;
    
    printf("To beat vampire methuselah's record, you need to live %d years more...\n", difference);

    return(0);
}
