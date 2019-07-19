#include "pch.h"
#include <iostream>

extern "C" int SignedMinA(int a, int b, int c); 
extern "C" int SignedMaxA(int a, int b, int c); 

extern "C" int SignedMinB(int a, int b, int c); 
extern "C" int SignedMaxB(int a, int b, int c); 

int main()
{
	int a, b, c;
	int min_a, max_a, min_b, max_b; 

	a = 1, b = 2, c = 3;
	
	min_a = SignedMinA(a, b, c);
	max_a = SignedMaxA(a, b, c);

	min_b = SignedMinB(a, b, c); 
	max_b = SignedMaxB(a, b, c); 

	printf("a = %d\n", a);
	printf("b = %d\n", b); 
	printf("c = %d\n\n", c); 

	printf("min_a = %d\n", min_a);
	printf("max_a = %d\n\n", max_a);

	printf("min_b = %d\n", min_b);
	printf("max_b = %d\n", max_b);

	return 0;
}