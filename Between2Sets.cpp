/* 
Week of Code 25. Betweeen 2 sets - https://www.hackerrank.com/contests/w25/challenges/between-two-sets/copy-from/7581136
*/

#include <iostream>
#include <vector>
#include <cassert>
#include <functional>// needed? for std:function though it compiles fine on my system without it.. there is reduce in function
using namespace std;

//declarations
//vector<int> plessthan100 = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};
int gcd(int,int);
int lcm(int,int);
int reduce(function<int (int,int)> ,vector<int>, int); // yipee!! i passed a function for the first time1
vector<int> primeslessthan(int);
int numfactors(int);


//functions
int main(){
    vector<int> v = {5,4,3,2,1};
    int res = reduce([](int x,int y){return x*y;},v,1);
    cout<<res<<endl;
    int n;
    int m;
    cin >> n >> m;
    vector<int> a(n);
    for(int a_i = 0;a_i < n;a_i++){
       cin >> a[a_i];
    }
    vector<int> b(m);
    for(int b_i = 0;b_i < m;b_i++){
       cin >> b[b_i];
    }
    int lcmA = reduce(lcm,a,a[0]);
    int gcdB = reduce(gcd,b,b[0]);
    if (gcdB%lcmA==0 && gcdB>=lcmA){// not sure this second condition is really needed. gcdB is never zero except B is all zeroes. should never because it messes up the lcm definition. Division by zero
        cout<<numfactors(gcdB/lcmA)<<endl;
    }
    else{
        cout<<0<<endl;
    }

    //tests
    /*
    cout<<lcm(3,3)<<endl;
    cout<<gcd(3,3)<<endl;
    vector<int> v = {8,16,1024};
    cout<<reduce(lcm,v)<<endl;
    cout<<numfactors(6)<<endl;
    */
}

int gcd(int a, int b){
    assert(a!=0 || b!=0); //check that they are both not zero. Important because 0%0 would give a divide by zero error
    if(a==0){
        return b;
    }
    return gcd(b%a,a);
}

int lcm(int a, int b){
    return (a*b)/gcd(a,b);
}

int reduce(function<int (int,int)> f,vector<int> v, int init){
    //applies the function to each pairwise elements in turn... not sure this ie extensive for other uses like... multiply numbers in an array together. The difference is the init
    int res = init;
    for(auto x : v){
        res=f(res,x);
    }
    return res;
}
vector<int> primeslessthan(int n){
    if(n==1){
        vector<int> v;
        return v;
    }
    vector<int> nums = vector<int>(n,1);
    vector<int> listofprimes ;
    nums[0]=nums[1]=0;
    int i = 2;
    while(i*i<n){
        if (nums[i]==1){
            //cout<<i<<" ";
            listofprimes.push_back(i);
            int k = 2*i;
            while (k<n){
                nums[k]=0;
                k+=i;
            }
            //incomplete function..
        }
        i+=1;
    }
    while(i<n){
        if (nums[i]==1){
            //cout<<i<<" ";
            listofprimes.push_back(i);
        }
        i+=1;
    }
return listofprimes;
}

int numfactors(int n){
    if (n==0){
        // or some other error condition
        return 0;
    }
    int res = 1;
    vector<int> plessthan100 = primeslessthan(100);
    for (auto x : plessthan100){
        int count = 0;
        while( n%x==0){
            n/=x;
            count+=1;
        }
        if(count>0){
            res*=(count+1);
        }
    }
    return res;
}