#include <iostream>

extern "C" int CalcArrayRowColSum(const int* x, int nRows, int nCols, int* row_sums, int* col_sums);

int main()
{
	const int nRows = 2, nCols = 3;

	// Initializing the value of the multi-dimensional arrays.
	int x[nRows][nCols] = {
		{1,2,3},
		{4,5,6},
		
	};

	int row_sums[nRows], col_sums[nCols]; 

	CalcArrayRowColSum((const int *)x, nRows, nCols, row_sums, col_sums);

	printf("Values by Rows:\n");
	for (int i = 0; i < nRows; i++)
	{
		for (int j = 0; j < nCols; j++)
		{
			printf("x[%d][%d] : %d\n", i, j, x[i][j]);
		}
		printf("\n"); // Prints newline after each row.
	}

	printf("Results by Rows:\n");
	for (int i = 0; i < nRows; i++)
	{
		printf("row_sum[%d] : %d\n", i, row_sums[i]);
	}

	printf("\nValues by Columns:\n");
	for (int i = 0; i < nCols; i++)
	{
		for (int j = 0; j < nRows; j++)
		{
			printf("x[%d][%d] : %d\n", j, i, x[j][i]);
		}
		printf("\n"); // Prints newline after each row.
	}

	printf("Result by Columns:\n");
	for (int i = 0; i < nCols; i++)
	{
		printf("col_sums[%d] : %d\n", i, col_sums[i]);
	}

	return 0;
}

