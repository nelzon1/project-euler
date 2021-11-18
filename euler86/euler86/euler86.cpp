using namespace std;
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

int dist(int a, int b, int c){
    return  a*a + b*b + c*c + (2 * b * c);
}

bool is_perfect_square(int n) {
	if (n < 0)
		return false;
	int root(round(sqrt(n)));
	return n == root * root;
}

int main(){
	int maxM = 5000;
    int setM = 1000000;      
    int solutions = 0;
    int currM = 1;
    while (solutions < setM && currM < maxM){
		currM += 1;
        for(int x = currM; x <= currM; x++){
            
            for(int y = 1; y <= x; y++){
                
                for(int z = 1; z <= y; z++ ) {
                    
                    int paths1 = dist(x,y,z);
                    int paths2 = dist(y,z,x);
                    int paths3 = dist(z,x,y);
                    
					int min = paths1;
					if (paths2 < paths1)
						min = paths2;
					if (paths3 < paths2 && paths3 < paths1)
						min = paths3;
					if (is_perfect_square(min))
						solutions++;
                }
            }
        }
    }
    cout << "Number of solutions: " << solutions << "\n" 
        << "Maximum M used: " << currM << "\n";

    system("pause");
}