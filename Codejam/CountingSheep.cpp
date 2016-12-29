/*
Problem Description - https://code.google.com/codejam/contest/dashboard?c=6254486#s=p0
*/

#include <set>
#include <iostream>

using namespace std;
int countSheep(int n){
    if(n==0){
        return 0;
    }
    set<int> myset;
    int p =0; //multiples of n
    int m =0; //keeps track of digits. goes to zero.
    while(myset.size()!=10){
        p+=n; //new multiple
        m=p;  
        while(m>0){
            myset.insert(m%10);
            m/=10;
        }
    }
    return p;
}
int main(){
    int num;
    int m;
    cin>>num;
    for(int i=1;i<num+1;i++){
        cin>>m;
        m = countSheep(m);
        if (m==0){
            cout<<"Case #"<<i<<":"<<" "<<"INSOMNIA"<<endl;
        }
        else{
            cout<<"Case #"<<i<<":"<<" "<<m<<endl;
        }
        
    }
}