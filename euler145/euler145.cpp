using namespace std;

#include <string>
#include <iostream>

string reverse(string str) {
	string rev = "";
	for (int i = 0; i < str.length(); i++) {
		rev.push_back(str.at(str.length() - i - 1));
	}
	return rev;
}


int main() {
	/*
	string test = "Jacob";
	string rev = reverse(test);
	cout << rev;
	int f;
	cin >> f;
	*/

	int count = 0;
	int limit = 1000000000;

	for (int i = 1; i <= limit; i++) {
		if (i % 10 == 0) {
			continue;
		}
		bool pure = true;
		string sum = to_string(i + stoi(reverse(to_string(i))));
		for (int j = 0; j < sum.length(); j++) {
			if ( (int) sum.at(j) % 2 == 0) {
				pure = false;
				break;
			}
		}
		if (pure) {
			count++;
		}
	}
	cout << "Number of reversible numbers below " << limit << ": " << count << ".\n";
	string end;
	cin >> end;


}