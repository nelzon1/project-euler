using namespace std;
#include <iostream>
#include <chrono>

long long gcd(long long x, long long y)
{
	do
	{
		if (x >= y) {
			x %= y;
		}
		else {
			y %= x;
		}
		if (y == 1 || x == 1)
			return 1;
	} while (x && y);

	return x + y;
}

double resilience(long d) {
	
	long denom = d - 1;
	long numer = 0;

	for (int i = 1; i < d; i++) {
		if (gcd(i, d) == 1) numer++;
	}

	return (double) numer / denom;
}

int main()
{
	long bestR = 1;
	long R = 1; 
	double bestRatio = 1.00;
	double curRatio = 1.00;
	double targetRatio = 0.22;
	cout << "Enter target resilience ratio:";
	cin >> targetRatio;	
	int end;
	cout << "Beginning search for lowest d with resillience " << targetRatio << ".\n";
	// Record start time
	auto start = chrono::high_resolution_clock::now();

	while (curRatio >= targetRatio) {
		R++;
		curRatio = resilience(R);
		if (curRatio < bestRatio) {
			bestRatio = curRatio;
			bestR = R;
		}
	}
	// Record end time
	auto finish = chrono::high_resolution_clock::now();
	chrono::duration<double> elapsed = finish - start;

	cout << "Lowest d: " << R << "\n" << "Resilience: " << curRatio << "\n";
	cout << "Elapsed time: " << elapsed.count() << " s\n";
	cin >> end;
}