#include "pch.h"
#include <iostream>

extern "C" int CalcArraySumASM(int *x, int n);

int CalcArraySumCPP(int *x, int n)
{
	int sum = 0;
	for (int i = 0; i < n; i++) 
	{
		sum += *x++;
	}

	return sum;
}

int main()
{
	int x[] = { 1, 2, 3, 4, 5 };
	int n = sizeof(x) / sizeof(int);
	int asm_sum, cpp_sum; 
	
	asm_sum = CalcArraySumASM(x, n);
	cpp_sum = CalcArraySumCPP(x, n);

	printf("Sizeof x	: %d\n", sizeof(x));
	printf("Sizeof int	: %d\n", sizeof(int));
	printf("Number of elements: %d\n\n", n);

	printf("Asm_sum : %d\n", asm_sum);
	printf("Cpp_sum : %d\n", cpp_sum);

	return 0;
}
