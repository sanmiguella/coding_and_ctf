#include <iostream>

extern "C" int NumFibVals;
extern "C" int MemoryAddressing(int i, int* v1, int* v2, int* v3, int *v4);

int main()
{
	for (int i = -1; i < NumFibVals + 1; i++)
	{
		int v1 = -1, v2 = -1, v3 = -1, v4 = -1;
		int rc = MemoryAddressing(i, &v1, &v2, &v3, &v4);

		printf("i: %2d, Return Code: %2d, ( ", i, rc);
		printf("v1: %5d , v2: %5d , v3: %5d , v4: %5d)\n", v1, v2, v3, v4);
	}

	return 0;
}

