
using namespace std;

#include <math.h>
#include <iostream>


int main()
{
	int collatz = 13;
	int count = 1;
	int countmax = 0;
	int number;
	for (int i = 1;i <= 1000000;i++)
	{
		collatz = i;
		while (collatz != 1)
		{
			
			if (collatz % 2 == 0)
				collatz /= 2;
			else collatz = 3 * collatz + 1;
			count++;
		}
		if (count > countmax)
		{
			countmax = count;
				number = i;
		}
		count = 1;
	}
	cout << "Number: " << number << " Chain: " << countmax;
	return 0;
}
