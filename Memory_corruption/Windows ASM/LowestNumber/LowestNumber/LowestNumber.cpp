#include "pch.h"
#include <iostream>

int main()
{
	const int rows = 2, cols = 3;
	int x[rows][cols] = { 
		{9, 4, 7}, 
		{11, 3, 10} 
	};

	int lowest_cpp = x[0][0]; // Lowest number starts at the beginning of the array.
	for (int i = 0; i < rows; i++)
	{
		printf("Row %d :\n", i);
		for (int j = 0; j < cols; j++)
		{
			printf("x[%d][%d] : %d\n", i, j, x[i][j]);

			int current_num = x[i][j];
			
			/*
			If the lowest number is greater than the current number,
			then the current number will be the lowest value.
			*/
			if (lowest_cpp > current_num) 
			{
				lowest_cpp = current_num;
			}
		}
		printf("\n");
	}

	printf("Results:\n");
	printf("Lowest number(cpp) is : %d\n", lowest_cpp);

	return 0;
}

