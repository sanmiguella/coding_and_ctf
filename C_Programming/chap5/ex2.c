#include <stdio.h>
#define BUF_SIZE 64

int main(void)
{
    char jerk[BUF_SIZE]; 
    
    puts("Name some jerk you know:"); 
    gets(jerk); 

    puts("\nYeah, i think..."); 
    puts(jerk); 
    puts("is a jerk, too.."); 

    return(0); 
}
