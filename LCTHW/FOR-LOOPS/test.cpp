#include <stdio.h>

int main(int argc, char* argv[]) {
	int i = 0;

	for (int i = 1; i < argc; i++) {
		printf("0x%p arg[%d]: %s\n", &argv[i], i, argv[i]);
	}

	const char *states[] = {
		"AAAA", "BBBB",
		"CCCC", "DDDD"
	};

	printf("\nSize of states -> %I64u\n", sizeof(states));
	printf("Size of each state -> %I64u\n", sizeof(states[0]));

	int number_of_states = sizeof(states) / sizeof(states[0]);
	printf("Number of states -> %d\n", number_of_states);

	printf("\n");
	for (int i = 0; i < number_of_states; i++) {
		printf("0x%p State[%d] -> %s\n", &states[i], i, states[i]);
	}

	return 0;
}