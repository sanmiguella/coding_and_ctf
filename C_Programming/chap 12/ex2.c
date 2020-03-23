#include <stdio.h>
#include <stdlib.h>
#define BUF_SIZE 2

int main()
{
    char num[BUF_SIZE];
    int number;

    puts("I am your computer genie!"); 
    printf("Enter a number from 0 to 9: ");
    fgets(num, BUF_SIZE, stdin);

    // Converts ascii to integer
    number = atoi(num); 

    if (number < 5)
    {
        puts("\nNumber is less than 5!");
    }

    else if (number == 5) 
    {
        puts("\nNumber is equals to 5!");
    }

    else if (number > 5)
    {
        puts("\nThat number is more than 5!");
    }

    puts("The genie knows all, sees all!");
    return(0);
}
