#include <iostream>
#include <vector>
using namespace std;

int newCandlesAdded(vector<int> v, int t, int n){
    int res = 0;
    int candyInBowl = n;
    for(int i = 0 ; i<t-1 ; i++){
        //cout<<candyInBowl<<" ";
        candyInBowl-=v[i];
        if (candyInBowl<5){
            res+=(n-candyInBowl);
            candyInBowl +=(n-candyInBowl);
        }
        
    }
    return res;
}

int main(){
    int n,t;
    cin>>n>>t;
    vector<int> v;
    for(int i=0;i<t;i++){
        int a;
        cin>>a;
        v.push_back(a);
        //cout<<a<<" ";
    }
    cout<<newCandlesAdded(v,t,n)<<endl;


}