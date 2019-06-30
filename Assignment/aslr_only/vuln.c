#include <stdio.h>
#include <string.h>

int main(int argc, char * argv[])
{
    char leaky[16];
    
    if(argc < 2)
    {
        printf("Please provide two arguments.\n");
        return 1;
    }

    memcpy(leaky, argv[1], 16);
    
    printf("Leaky buffer: %s\n", leaky);
    printf("another round? : ");
    fgets(leaky, 64, stdin);

    return 0;
}
