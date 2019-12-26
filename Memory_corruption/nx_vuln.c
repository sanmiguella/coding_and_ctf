#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void overflow() {
	char buffer[128];

	printf("Enter something :\n");
	gets(buffer);

	printf("\nYou entered :\n%s\n", buffer);
}

int main()
{
	overflow();
	return(0);
}
