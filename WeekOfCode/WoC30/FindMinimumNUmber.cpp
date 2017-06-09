#include <bits/stdc++.h>
#include <string>

using namespace std;

string findminstr(int n){
    if (n==2){
        return "min(int, int)";
    }
    return "min(int, "+findminstr(n-1)+")";
}
int main(){
    int n;
    cin >> n;
    cout<<findminstr(n);
    return 0;
}
