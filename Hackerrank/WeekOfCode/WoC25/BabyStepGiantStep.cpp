/*
Week of Code 25 - https://www.hackerrank.com/contests/w25/challenges/baby-step-giant-step/copy-from/7613913
*/

#include <iostream>
using namespace std;


int main(){
    int q;
    cin>>q;
    for(int i=0; i<q; i++){
        int a,b,d;
        cin>>a>>b>>d;
        int count = 0;
        count = d>2*b? (d - 2*b)/b+1 : 0 ;
        int left = (d-count*b);
        if(left==b || left==a){
            cout<<count+1;
        }else if (b<left<2*b || 0<left<b){
            cout<<count+2;
        }else if (left==0){
            cout<<count;
        }
    }
}
