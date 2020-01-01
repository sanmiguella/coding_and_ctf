#include <iostream>

/*
	  Y  0  1  2
	X    
	0    *  *  *
	1	 *  *  *
	2	 *  *  *
*/

void CalcArrayCube(int* y, const int* x, int nRows, int nCols)
{
	// Row : Horizontal, Looping through rows.
	for(int i = 0; i < nRows; i++)
	{
		// Column : Vertical, Looping through columns.
		for (int j = 0; j < nCols; j++)
		{
			/*
				(0 x 3 + 0) = 0, (0 x 3 + 1) = 1,  (0 x 3 + 2) = 2
				(1 x 3 + 0) = 3, (1 x 3 + 1) = 4,  (1 x 3 + 2) = 5
				(2 x 3 + 0) = 6, (2 x 3 + 1) = 7,  (2 x 3 + 2) = 8
				(3 x 3 + 0) = 9, (3 x 3 + 1) = 10, (3 x 3 + 2) = 11
			*/
			int k = i * nCols + j; 
			y[k] = x[k] * x[k] * x[k]; 
		}
	}
}

int main()
{
	const int nRows = 4;
	const int nCols = 3;

	// Initializing the values.
	int x[nRows][nCols] = {
		{1,2,3},
		{4,5,6},
		{7,8,9},
		{10,11,12}
	};

	// Holds the cube value.
	int y[nRows][nCols];

	// void CalcArrayCube(int* y, const int* x, int nRows, int nCols)
	CalcArrayCube(&y[0][0], &x[0][0], nRows, nCols);

	for(int i = 0; i < nRows; i++)
	{
		for (int j = 0; j < nCols; j++)
		{
			/*
				[0][0], [0][1], [0][2] 
				[1][0], [1][1], [1][2]
				[2][0], [2][1], [2][2]
				[3][0], [3][1], [3][2]
			*/
			printf("(%2d, %2d) : %6d, %6d\n", i, j, x[i][j], y[i][j]);
		}
	}
}

