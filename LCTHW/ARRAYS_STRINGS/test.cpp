#include <stdio.h>

int main(int argc, char* argv[]) {
	int areas[] = { 10,12,13,14,20 };
	char name[] = "AABB"; 
	char full_name[] = {
		'A','A','B','B',
		'C','C','D','D','\0'
	};

	printf("The size of an int: %I64u\n", sizeof(int));
	printf("The size of (0x%p) areas (int []): %I64u\n", areas, sizeof(areas));
	printf("The number of ints in areas: %I64u\n", sizeof(areas) / sizeof(int));
	printf("The 1st area is %d, the 2nd area is %d\n", areas[0], areas[1]);

	printf("The size of a char: %I64u\n", sizeof(char));

	printf("\n");
	for (int i = 0; i < sizeof(name); i++) {
		printf("0x%p name[%d] -> %c (0x%x)\n", &name[i], i, name[i], name[i]);
	}

	printf("\nThe size of name (char []): %I64u\n", sizeof(name));
	printf("The number of chars: %I64u\n", sizeof(name) / sizeof(char));

	printf("\n");
	for (int i = 0; i < sizeof(full_name); i++) {
		printf("0x%p full_name[%d] -> %c (0x%x)\n", &full_name[i], i, full_name[i], full_name[i]);
	}

	printf("\nThe size of full_name (char []): %I64u\n", sizeof(full_name));
	printf("The number of chars: %I64u\n", sizeof(full_name) / sizeof(char));

	printf("\nname = \"%s\" and full_name = \"%s\"", name, full_name);
	return 0;
}