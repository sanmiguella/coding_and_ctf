#include <stdio.h>
#include <stdlib.h>

#define HEIGHT_SIZE 4
#define TEMP_SIZE   4
#define FAVNUM_SIZE 5

int main()
{
    int tax1, tax2;
    char height[HEIGHT_SIZE], temp[TEMP_SIZE], favnum[FAVNUM_SIZE]; 

    printf("Enter your height in inches: "); 
    fgets(height, HEIGHT_SIZE, stdin); 

    printf("What temperature is it outside? ");
    fgets(temp, TEMP_SIZE, stdin); 

    printf("Enter your favorite number: ");
    fgets(favnum, FAVNUM_SIZE, stdin);

    // tax1 = int(height) * int(favnum)
    tax1 = atoi(height) * atoi(favnum);

    // tax2 = int(temp) * int(favnum) 
    tax2 = atoi(temp) * atoi(favnum);


    if (tax1 > tax2)
    {
        printf("\nYou owe $%d in taxes.\n", tax1*10);
    }

    else if (tax2 > tax1)
    {
        printf("\nYou owed $%d in taxes.\n", tax2*10);
    }

    return(0);
}
