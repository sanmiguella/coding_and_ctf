#include <stdio.h>
#define BUF_SIZE 64

int main(void)
{
    int age;
    char name[BUF_SIZE]; 

    printf("Whats is your age? "); 
    scanf("%d", &age); 

    printf("What is your name? ");
    scanf("%s", name); 

    printf("%s is %d years old..\n", name, age); 
    return(0);
}
