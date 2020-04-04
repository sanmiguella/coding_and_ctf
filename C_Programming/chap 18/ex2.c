#include <stdio.h>

int main() {
    int start;
   
    puts("Initial start(1 to 10)"); 
    printf("Please enter number to start: ");
    
    scanf("%d",&start);
    
    if(start>0 && start<11) {
        printf("\n");

        do
        {
            printf("Countdown -> %d\n",start);
            start--;
        } 
        while(start>0);
        
        printf("\nZero!!\n");
        puts("Blast off!!");
    }

    else {
        puts("\nInput must be between 1 to 10");
    }
}
