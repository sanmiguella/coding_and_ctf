#include "pch.h"
#include <iostream>

extern "C" int CountChar(wchar_t *s, wchar_t c);

int main()
{
	/*
		2 A's
		3 B's
		4 C's
		5 D's
	*/
	wchar_t *string;
	wchar_t char_to_search;
	int found = 0;

	// Initializing variable with values.

	/*
		A : \x41
		B : \x42
		C : \x43
		0 : \x30
	*/
	string = (wchar_t *) L"AA00BBCC";
	char_to_search = L'0';
	found = CountChar(string, char_to_search);

	/*
		%s : string
		%c : char
		%d : integer
	*/
	wprintf(L"Test string : %s\n", string);
	wprintf(L"Char to search : %c\n", char_to_search);
	printf("Found char count : %d\n", found);

	return 0;
}

