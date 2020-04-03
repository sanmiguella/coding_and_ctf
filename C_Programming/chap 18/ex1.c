#include <stdio.h>

int main() {
    int start;
    
    printf("Please enter the number to start\n");
    printf("The countdown (1 to 5):");
    scanf("%d",&start);
   
    printf("\n"); 
    // Countdown loop
    do 
    {
        printf("T-minus %d\n",start);
        start--;
    }
    while(start>0);

    printf("\nZero!\nBlast off!\n");
    return(0);
}
