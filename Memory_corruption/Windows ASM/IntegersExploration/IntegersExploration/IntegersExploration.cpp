#include "pch.h"
#include <iostream>

extern "C" char GlChar = 10; 
extern "C" short GlShort = 20; 
extern "C" int GlInt = 30; 
extern "C" long long GLongLong = 0x00000000FFFFFFFF;

extern "C" void IntegerAddition(char a, short b, int c, long long d);

int main()
{
	IntegerAddition(5, 5, 5, 0xCAFEBABF00000000);

	printf("Char Value: %d\n", GlChar);
	printf("Short Value: %d\n", GlShort);
	printf("Int Value : %d\n", GlInt);
	printf("Long Value : 0x%llX\n", GLongLong);
	
	return 0;
}
