#include "pch.h"
#include <iostream>

extern "C" void integer_division_asm(int a, int b, int *quotient, int *remainder);

int main()
{
	int a = 5, b = 2; 
	int quotient, remainder;

	printf("Values:\n"); 
	printf("a: %4d\n", a);
	printf("b: %4d\n", b);

	integer_division_asm(a, b, &quotient, &remainder);

	printf("\nResults(asm):\n");
	printf("quo: %4d\n", quotient);
	printf("rem: %4d\n", remainder);

	return 0;
}

