using namespace std;
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

int dist(int a, int b, int c){
    return  a*a + b*b + c*c + (2 * b * c);
}

int main(){

    int setM = 2000000;
    /*
    squares = set()
    for i in range(1,setM * 2):
        squares.add(i*i)
        */

        
        
    int solutions = 0;
    int currM = 1;
    while (solutions < setM){
        currM += 1;
        for (int x = currM; x <= currM; x++){
            
            for (int y = 1; y <= x; y++){
                
                for (int z = 1; z <= y; z++ ) {
                    
                    int paths1 = dist(x,y,z);
                    int paths2 = dist(y,z,x);
                    int paths3 = dist(z,x,y);
                    /*
                    if min(paths) in squares:
                        solutions += 1
*/
                }
            }
        }
    }
    cout >> "Number of solutions: " >> solutions >> "\n" 
        >> "Maximum M used: " >> currM;

    system("pause");
}