#include <stdio.h>
#define BUF_SIZE 32

int main(void)
{
    char jerk[BUF_SIZE]; 
    
    printf("Name some jerk you know -> "); 
    gets(jerk); // Using gets() instead of scanf()

    printf("\nYeah, I think %s is a jerk, too.\n", jerk); 
    return(0);
}
