#include <stdio.h>

int add(int a, int b);

int main() {
    int a = 1, b = 2, total; 

    total = add(a, b);
    printf("%d + %d = %d\n", a, b, total); 
   
    return(0);
}

int add(int a, int b) {
    return(a + b);
}
