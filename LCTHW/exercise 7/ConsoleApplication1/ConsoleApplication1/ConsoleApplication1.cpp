#include <stdio.h>

int main(int argc, char* argv[]) {
	int distance = 100; 
	float power = 2.345f; 
	double super_power = 56789.4532; 
	char initial = 'A'; 
	char first_name[] = "zed"; 
	char last_name[] = "shaw";

	printf("Argument count : %d\n", argc);
	for (int count = 0; count < argc; count++) {
		printf("0x%p - argv[%d] {%d bytes} : %s\n", 
			&argv[count], count, sizeof(argv[count]) ,argv[count]);
	}

	printf("\n");
	printf("0x%p (%d bytes) - You are %d miles away.\n", &distance, sizeof(distance), distance); 
	printf("0x%p (%d bytes) - You have %f levels of power.\n", &power, sizeof(power),power); 
	printf("0x%p (%d bytes) - You have %f awesome super powers.\n", &super_power, sizeof(super_power), super_power);
	printf("0x%p (%d byte) - I have an initial %c.\n", &initial, sizeof(initial), initial);
	printf("0x%p (%d bytes) - I have a first name %s.\n", &first_name, sizeof(first_name), first_name); 
	printf("0x%p (%d bytes) - I have a last name %s.\n\n", &last_name, sizeof(last_name), last_name); 
	printf("My whole name is %s(0x%p) %c(0x%p). %s(0x%p)\n\n",
		first_name, &first_name, 
		initial, &initial,
		last_name, &last_name);

	int bugs = 100; 
	double bug_rate = 1.2; 

	printf("You have %d(0x%p) {%d bytes} bugs at the imaginary rate of %f(0x%p) {%d bytes}.\n\n",
		bugs, &bugs, sizeof(bugs),
		bug_rate, &bug_rate, sizeof(bug_rate));

	long universe_of_defects = 1L * 1024L * 1024L * 1024L;
	printf("The entire universe has %ld(0x%p) {%d bytes} bugs.\n\n", 
		universe_of_defects, &universe_of_defects, sizeof(universe_of_defects));

	double expected_bugs = bugs * bug_rate; 
	printf("You are expected to have %f(0x%p) {%d bytes} bugs.\n\n", 
		expected_bugs, &expected_bugs, sizeof(expected_bugs)); 

	double part_of_universe = expected_bugs / universe_of_defects; 
	printf("That is only a %e(0x%p) {%d bytes} portion of the universe.\n\n", 
		part_of_universe, &part_of_universe, sizeof(part_of_universe));

	char null_byte = '\0'; 
	printf("Null Byte : 0x%x(0x%p) {%d byte}\n\n", null_byte, &null_byte, sizeof(null_byte));

 	int care_percentage = bugs * null_byte;
	printf("Which means you should care %d%%(0x%p) {%d bytes}.\n", 
		care_percentage, &care_percentage, sizeof(care_percentage));

	return 0;
}