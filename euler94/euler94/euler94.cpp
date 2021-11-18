
using namespace std;

#include <iostream>
#include <cmath>

double heron(int a, int b, int c) {
	double s = (a + b + c) / 2.0;
	return sqrt(s*(s - a)*(s - b)*(s - c));
}

int isPerfectSquare(long long int n)
{
	int h = n & 0xF;  // h is the last hex "digit"
	if (h > 9)
		return 0;
	// Use lazy evaluation to jump out of the if statement as soon as possible
	if (h != 2 && h != 3 && h != 5 && h != 6 && h != 7 && h != 8)
	{
		int t = (int)floor(sqrt((double)n) + 0.5);
		return t * t == n;
	}
	return 0;
}


int main()
{
	long long int N = 10000000;
	int totalsum = 0;

	//for (int i = 1; i < N; i++) {
	//	if (i * 3 + 1 > N) {
	//		cout << "Exceeded limit: " << N << "\n";
	//		break;
	//	}
	//	if (fmod(heron(i,i,i+1),1.0) == 0) {
	//		totalsum += i * 3 + 1;
	//	}
	//	if (fmod(heron(i, i+1, i + 1), 1.0) == 0) {
	//		totalsum += i * 3 + 2;
	//	}
	//}

	//for (long long int i = 1000000000; i < 1001000000; i++) {
	//	if (isPerfectSquare(i) == 1)
	//		cout << "Perfect square: " << i << '\n';
	//}

	for (int i = 1; i * 3 + 1 <= N; i++) {
		double s1 = i * 3 + 1 / 2.0;
		double s2 = i * 3 + 2 / 2.0;
		long long int area1 = s1 * (s1 - i)*(s1 - i)*(s1 - i - 1);
		long long int area2 = s2 * (s2 - i)*(s2 - i - 1)*(s2 - i - 1);
		if (isPerfectSquare(area1) == 1) {
			totalsum += i * 3 + 1;
		}
		if (isPerfectSquare(area2) == 1) {
			totalsum += i * 3 + 2;
		}
	}


	int test;
	cout << "Total sum: " << totalsum;
	cin >> test;
}

