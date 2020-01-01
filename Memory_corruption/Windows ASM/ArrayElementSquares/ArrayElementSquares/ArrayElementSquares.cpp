#include "pch.h"
#include <iostream>

/*
	y - output array, 
	x - input array, 
	n - length of array
*/

extern "C" int CalcArraySquaresASM(int *y, int *x, int n);
int CalcArraySquaresCPP(int *y, int *x, int n);

int main()
{
	int x[] = { 1, 2, 3, 4, 5 };			// Initializes the x[] array.
	const int n = sizeof(x) / sizeof(int);	// Determines the size of the array.
	int y_asm[n];							// y[] array for asm.
	int y_cpp[n];							// y[] array for cpp.
	int asm_sum, cpp_sum;					// To hold the sum value for both asm and cpp function.

	asm_sum = CalcArraySquaresASM(y_asm, x, n);
	cpp_sum = CalcArraySquaresCPP(y_cpp, x, n);

	printf("sizeof(x) : %d\n", sizeof(x));
	printf("sizeof(int) : %d\n", sizeof(int));
	printf("sizeof(x) / sizeof(int) : %d\n\n", n);

	printf("\nasm_sum : %d\n", asm_sum);
	printf("cpp_sum : %d\n", cpp_sum);

	return 0;
}

int CalcArraySquaresCPP(int *y, int *x, int n) 
{
	int sum = 0;			// Intializes sum because sum needs to be zero for the return values to be correct.
	
	for (int i = 0; i < n; i++)
	{
		y[i] = x[i] * x[i]; // Determine the square of 'x' and copies value of to 'y'.
		sum += y[i];		// For each loop, the current value of 'y' is added to sum.
	}

	return sum;				// Returns sum to the calling function.
}