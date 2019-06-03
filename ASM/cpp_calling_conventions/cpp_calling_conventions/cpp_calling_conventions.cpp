#include "pch.h"
#include <iostream>

// Declare Assembly function prototype 
extern "C" void calculate_sum(int a, int b, int c, int *s1, int *s2, int *s3);

int main()
{
	int a = 2, b = 3, c = 4;
	int s1, s2, s3; 

	// &s1 means passing the address of 's1' into the function
	calculate_sum(a, b, c, &s1, &s2, &s3);

	printf("Input a: %4d\n", a);
	printf("Input b: %4d\n", b);
	printf("Input c: %4d\n\n", c);
	printf("Output s1(sum): %4d\n", s1);
	printf("Output s2(square): %4d\n", s2);
	printf("Output s3(cube): %4d\n", s3);

	return 0;
}

