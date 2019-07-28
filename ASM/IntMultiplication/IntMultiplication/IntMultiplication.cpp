#include "pch.h"
#include <iostream>

extern "C" int multiply_asm(int a, int b); 
int multiply_cpp(int a, int b);

int main()
{
	int a = 3, b = 4; 
	int result = multiply_cpp(a, b); 

	printf("Values:\n");
	printf("a : %d\n", a);
	printf("b : %d\n\n", b);

	printf("Results:\n");
	printf("(cpp) : %d\n", result);

	int result_asm = multiply_asm(a, b); 
	printf("(asm) : %d\n", result_asm);

	return 0;
}

int multiply_cpp(int a, int b)
{
	return a * b;
}