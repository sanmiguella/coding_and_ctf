#include <stdio.h>

int main() {
    char selection; 

    printf("Please make your treat selection:\n"); 
    printf("1 - Beverage.\n");
    printf("2 - Candy.\n"); 
    printf("3 - Hot dog.\n");
    printf("4 - Popcorn.\n");
    printf("Your choice: ");

    selection = getchar(); 
    
    switch(selection)
    {
        case '1':
            printf("\nBeverage\nThat will $8.00\n");
            break; 
        
        case '2':
            printf("\nCandy\nThat will be $5.50\n");
            break;

        case '3':
            printf("\nHot dog\nThat will be $10.00\n");
            break;

        case '4':
            printf("\nPopcorn\nThat will be $7.50\n");
            break; 

        default:
            printf("\nThat is not a proper selection.\n");
            printf("I'll assume you're just not hungry.\n"); 
            printf("Can i help whoever's next?\n");
    }

    return(0);
}
