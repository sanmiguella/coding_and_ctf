#include <stdio.h>

int main(void) {
    printf("This is a \"text\" enclosed in double quotation..\n"); 
    printf("This is a \\text\\ enclosed in backslashes..\n");
   
    int age = 10;           
    char *name = "tom";     // Declaration of a string
    
    printf("My name is %s, and i am %d years old..\n", name, age);
    return(0);
}
