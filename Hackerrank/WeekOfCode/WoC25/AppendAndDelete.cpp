/*
Week of Code 25 - https://www.hackerrank.com/contests/w25/challenges/append-and-delete/

*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int countCommon(string s,string t ){
    int count = 0;
    int minl = min(s.size(),t.size());
    while(count<minl&&s[count]==t[count]){
        count+=1;
    }
    return count;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    string s;
    string t;
    int k;
    cin>>s;
    cin>>t;
    cin>>k;
    if (k>=(s.size()+t.size())){
        cout<<"Yes"<<endl;
    }else if (k>=(s.size()-2*countCommon(s,t)+t.size()) && ((k-(s.size()-2*countCommon(s,t)+t.size()))%2==0)){
        cout<<"Yes"<<endl;
    }else{
        cout<<"No"<<endl;
    }
    return 0;
}
