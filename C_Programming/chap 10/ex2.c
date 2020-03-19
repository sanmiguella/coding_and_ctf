#include <stdio.h>
#include <stdlib.h>
#define CONVERT_TO_METERS 3.281

int main()
{
    float height_in_meters; 
    char height_in_foot[2]; 

    printf("Enter your height in foot -> "); 
    gets(height_in_foot);
    
    height_in_meters = atoi(height_in_foot) / CONVERT_TO_METERS;
    printf("You are %.2f meters tall.\n", height_in_meters);

    return(0);
}
