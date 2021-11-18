// euler69_2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <math.h>
#include <string>
#include <iostream>
#include <time.h>

using namespace std;



int gcf(int a, int b)
{
	int d = 0;
	while ((a % 2 == 0) && (b % 2 == 0))
	{
		a = a / 2;
		b = b / 2;
		d++;
	}
	while (a != b)
	{
		if (a % 2 == 0)
			a = a / 2;
		else if (b % 2 == 0)
			b = b / 2;
		else if (a > b)
			a = (a - b) / 2;
		else
			b = (b - a) / 2;
	}
	return a * pow(2, d);
}

int totient(int a)
{
	int t = 1;
	if (a % 2 == 1)
		t++;
	for (int i = 3; i < a; i++)
	{
		if (gcf(i, a) == 1)
			t++;
	}
	return t;
}	

int main()
{

	int t0 = time(NULL);


	int n = 1000000;
	int tote, func;
	int max = 2;
	int max_int, max_tote;
	for (int i = 2; i < n;i++)
	{
		tote = totient(i);
		func = i / float(tote);

		if (func > max)
		{
			max = func;
			max_int = i;
			max_tote = tote;
		}
	}

	cout << "Max n/phi(n): " + std::to_string(max) + '\t' + "Max n: " + std::to_string(max_int) + '\n' + "";
	int t1 = time(NULL);
	cout << "Size of set: " << std::to_string(n) << '\n';

	printf("time = %d secs\n", t1 - t0);
	return 0;
}