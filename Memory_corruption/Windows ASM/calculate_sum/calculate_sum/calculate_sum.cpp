#include "pch.h"
#include <iostream>

extern "C" int adder_ASM(int a, int b, int c); 
int adder_CPP(int a, int b, int c); // Function prototype

int main()
{
	int a = 17, b = 11, c = 14;	// Variable declaration
	int sum = adder_CPP(a, b, c); // Using Functions in CPP

	printf("--- Using CPP functions ---\n");
	printf("a: %d\n", a); 
	printf("b: %d\n", b); 
	printf("c: %d\n", c); 
	printf("sum_cpp: %d\n\n", sum);

	int sum_asm = adder_ASM(a, b, c);
	printf("--- Using ASM functions ---\n"); 
	printf("a: %d\n", a);
	printf("b: %d\n", b);
	printf("c: %d\n", c);
	printf("sum_asm: %d\n", sum_asm);

	return 0; 
}

int adder_CPP(int a, int b, int c) // CPP Functions
{
	return a + b + c;
}