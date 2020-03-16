#include <stdio.h>
#include <stdlib.h>
#define BUF_SIZE 8 

int main(void)
{
    int age;
    char years[BUF_SIZE]; 
    
    printf("How old is the methuselah vampire? "); 
    gets(years); 

    age = atoi(years);
    printf("Methuselah vampire was %d years old.\n", age);

    return(0);
}
