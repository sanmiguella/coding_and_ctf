#include "pch.h"
#include <iostream>

extern "C" void CopyStrAsm(char *msg, char *copy, int msg_size);

int main()
{
	char msg[] = "ABCDEF";
	const int msg_size = sizeof(msg);
	char copy[msg_size];

	printf("msg : %s\n", msg);
	printf("msg_size : %d\n\n", msg_size);

	CopyStrAsm(msg, copy, msg_size);

	printf("copy[] : %s\n", copy);

	return 0; 
}
