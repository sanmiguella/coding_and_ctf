#include <stdio.h>
#define BUF_SIZE 64

int main(void)
{
    char jerk[BUF_SIZE]; 
    
    puts("[+] Name some jerk you know.."); 
    gets(jerk); 

    printf("[!] Yeah, I think %s is a jerk too..\n", jerk); 
    return(0); 
}
