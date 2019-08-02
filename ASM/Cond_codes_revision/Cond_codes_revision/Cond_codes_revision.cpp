#include "pch.h"
#include <iostream>

extern "C" int SignedMaxA_asm(int a, int b, int c);
int SignedMaxA_cpp(int a, int b, int c);

int main()
{
	int a = 4, b = 5, c = 3;
	int max_cpp = SignedMaxA_cpp(a, b, c);
	int max_asm = SignedMaxA_asm(a, b, c);

	printf("a: %d\n", a);
	printf("b: %d\n", b);
	printf("c: %d\n", c); 
	printf("\nMax(cpp): %d\n", max_cpp);
	printf("Max(asm): %d\n", max_asm);

	return 0;
}

int SignedMaxA_cpp(int a, int b, int c)
{
	int largest; 

	if (a > b)
	{
		/*
			If 'a' > 'b' THEN 'a' is the largest.
			If 'a' < 'c' THEN 'c' is the largest, else do nothing bout it because 'a' is still the largest. 
		*/
		largest = a; 
	}

	else if (b > a)
	{
		/*
			IF 'b' > 'a' THEN 'b' is the largest. 
			IF 'b' < 'c' THEN 'c' is the largest, else do nothing bout it because 'b' is still the largest.
		*/
		largest = b; 
	}

	if (c > largest)
	{
		/*
			IF 'c' > 'a' or 'b', THEN 'c' is the largest.
		*/
		largest = c;
	}

	return largest; // Return to the calling function the largest among the 3.
}

