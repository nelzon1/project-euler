// euler95.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdio.h"
#include <cmath>
#include <vector>
#include <iostream>
using namespace std;

int divSum(int num)
{
	// Final result of summation of divisors 
	int result = 0;

	// find all divisors which divides 'num' 
	for (int i = 2; i <= sqrt(num); i++)
	{
		// if 'i' is divisor of 'num' 
		if (num%i == 0)
		{
			// if both divisors are same then add 
			// it only once else add both 
			if (i == (num / i))
				result += i;
			else
				result += (i + num / i);
		}
	}

	// Add 1 to the result as 1 is also a divisor 
	return (result + 1);
}

bool vecIn(std::vector<int> myVec, int x) {
	for (int i = 0; i < myVec.size(); i++) {
		if (myVec[i] == x) return true;
	}
	return false;
}

std::vector<int> chain(int startNum) {
	std::vector<int> theChain {startNum};
	int nextItem = divSum(startNum);
	while (nextItem <= startNum * 100 || nextItem <= 1000000) {
		if (nextItem == theChain[0]) {
			return theChain;
		}
		else if (vecIn(theChain,nextItem) ){
			return std::vector<int> (0);
		}
		theChain.push_back(nextItem);
		nextItem = divSum(nextItem);
	}
	return std::vector<int>(0);
}

void printVector(std::vector<int> vec) {
	for (std::vector<int>::size_type i = 0; i != vec.size(); i++) {
		cout << vec[i] << ", ";
	}
	cout << '\n';
}

int main()
{
	int N = 1000000;

	for (int i = 1; i < N; i++) {
		std::vector<int> curvec = chain(i);
		if (curvec.size() > 0) {
			printVector(curvec);
		}
		//cout << i << "\n";
	}
	//printVector(chain(122410));
	cout << "Complete up to " << N << '\n';
}

