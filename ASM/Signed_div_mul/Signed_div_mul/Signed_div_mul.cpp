#include "pch.h"
#include <iostream>

// Prod - product(multiplication), Quo - quotient(result of division), Rem - remainder(remainder of division)
extern "C" int integer_mul_div(int a, int b, int *prod, int *quo, int *rem);

int main()
{
	int a = 21, b = 9; 
	int prod = 0, quo = 0, rem = 0; 
	int rv; 

	rv = integer_mul_div(a, b, &prod, &quo, &rem);

	printf("Input a : %4d\n", a);
	printf("Input b : %4d\n", b);
	printf("Multiply Result - Prod : %4d\n\n", prod);

	printf("Input a : %4d\n", a);
	printf("Input b : %4d\n", b);
	printf("Division Result - Quo : %4d\n", quo);
	printf("Division Result - Rem : %4d\n", rem);

	return 0;
}



