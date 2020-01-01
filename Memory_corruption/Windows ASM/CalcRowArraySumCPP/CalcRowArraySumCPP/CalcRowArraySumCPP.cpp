#include <iostream>

void CalcArrayRowColSum(const int* x, int nRows, int nCols, int* row_sums, int* col_sums)
{
	/*
		 1,  2,  3
		 4,  5,  6
		 7,  8,  9
		10, 11, 12
	*/

	for (int i = 0; i < nRows; i++)		// Calculate row_sums: Outer Loop
	{
		row_sums[i] = 0; 
		for (int j = 0; j < nCols; j++)	// Calculate row_sums: Inner Loop
		{
			/*
				(0 * 3) + 0 = 0, (0 * 3) + 1 = 1,  (0 * 3) + 2 = 2
				(1 * 3) + 0 = 3, (1 * 3) + 1 = 4,  (1 * 3) + 2 = 5
				(2 * 3) + 0 = 6, (2 * 3) + 1 = 7,  (2 * 3) + 2 = 8
				(3 * 3) + 0 = 9, (3 * 3) + 2 = 10, (3 * 3) + 2 = 11
			
			*/
			int k = (i * nCols) + j;
			row_sums[i] += x[k];
		}
	}

	/*
		 1,  2,  3
		 4,  5,  6
		 7,  8,  9
		10, 11, 12
	*/

	for (int i = 0; i < nCols; i++)
	{
		col_sums[i] = 0;

		for (int j = 0; j < nRows; j++)
		{
			/*
				i = 0
				j = 0, k = (0 x 3) + 0 = 0
				j = 1, k = (1 x 3) + 0 = 3
				j = 2, k = (2 x 3) + 0 = 6
				j = 3, k = (3 x 3) + 0 = 9

				i = 1
				j = 0, k = (0 x 3) + 1 = 1
				j = 1, k = (1 x 3) + 1 = 4
				j = 2, k = (2 x 3) + 1 = 7
				j = 3, k = (3 x 3) + 1 = 10

				i = 2
				j = 0, k = (0 x 3) + 2 = 2
				j = 1, k = (1 x 3) + 2 = 5
				j = 2, k = (2 x 3) + 2 = 8
				j = 3, k = (3 x 3) + 2 = 11
			*/

			int k = (j * nCols) + i;
			col_sums[i] += x[k];
		}
	}
}

int main()
{
	const int nRows = 4;
	const int nCols = 3;

	int x[nRows][nCols] = {
		{1,2,3},
		{4,5,6},
		{7,8,9},
		{10,11,12}
	};

	int row_sums[nRows];
	int col_sums[nCols];

	CalcArrayRowColSum(&x[0][0], nRows, nCols, &row_sums[0], &col_sums[0]);

	/*
		1 + 2 + 3 = 6
		4 + 5 + 6 = 15
		7 + 8 + 9 = 24 
		10 + 11 + 12 = 33
	*/

	for (int i = 0; i < nRows; i++)
	{
		printf("Sum of row[%d] : %d\n", i + 1, row_sums[i]);
	}

	printf("\n");
	for (int i = 0; i < nCols; i++)
	{
		printf("Sum of cols[%d] : %d\n", i + 1, col_sums[i]);
	}

	return 0;
}

