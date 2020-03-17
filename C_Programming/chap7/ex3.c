#include <stdio.h>
#include <stdlib.h>
#define METHU_AGE 969
#define BUF_SIZE 8

int main()
{
    int contributed, received;
    char work_age[BUF_SIZE];
    char retire_age[BUF_SIZE];
    
    printf("When did methuselah start working? "); 
    scanf("%s", work_age); 

    printf("When did methuselah stop working? "); 
    scanf("%s", retire_age); 

    contributed = atoi(retire_age) - atoi(work_age); 
    received = METHU_AGE - atoi(retire_age); 

    printf("\nMethuselah contributed to social security for %i years.\n", contributed); 
    printf("Methuselah collected from social security for %i years.\n", received); 

    return(0);
}
