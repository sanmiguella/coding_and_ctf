#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
	if (argc != 2) {
		printf("ERROR: You need one argument.\n"); 
		return 1;
	}

	for (int i = 0; i < argc; i++) {
		printf("Arg %d : 0x%p -> %s\n", i, &argv[i], argv[i]);
	}

	printf("\n");

	char* ptr_first_arg = argv[1];

	// How it works:
	//	Example string -> BaBa
	//	ptr_first_arg will point to a letter in the string 'BaBa'
	//	Where it will point will be determined by the current iteration of the for loop.
	//	If the letter being pointed to is lowercase, convert it to uppercase, else do nothing.
	for (int i = 0; *ptr_first_arg != '\0'; i++) {
		char letter = *ptr_first_arg; 
		int letter_as_int = int(letter);

		// Ascii table:
		//	https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html
		if (letter_as_int >= 97 && letter_as_int <= 122) {
			letter_as_int -= 32; 
			letter = char(letter_as_int);	 
			*ptr_first_arg = char(letter);
		}

		printf("0x%p -> %c(0x%02x) : %d\n", ptr_first_arg, *ptr_first_arg, *ptr_first_arg, int(*ptr_first_arg));
		ptr_first_arg++;
	}

	return 0;
}