#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int query(vector<int> A, int x, int y){
    int countx = 0;
    int county = 0;
    unordered_map<int, int> difference ;
    for(int i = 0; i<A.size(); i++){
        if(A[i] == x){
            countx += 1;
        }
        if(A[i] == y){
            county += 1;
        }
        difference[countx-county] = difference[countx-county]+1;
    }
    int ans = 0;
    

}
int main(){

}