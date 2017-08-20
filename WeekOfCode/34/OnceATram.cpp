#include <iostream>
#include <vector>
using namespace std;
int sumdigits(int n){
    int s = 0;
    while(n > 0){
        s += (n%10);
        n /= 10;
    }
    return s;
}

int nextLuckyNumber(int n){
    for(int i = n+1; i<1000000; i++){
        int first = i/1000;
        int second = i%1000;
        int sumfirst = sumdigits(first);
        int sumsecond = sumdigits(second);
        if (sumfirst == sumsecond){
            return i;
        }
    }
    return -1;
}
int main(){
    int n;
    cin>>n;
    cout<<nextLuckyNumber(n);
}