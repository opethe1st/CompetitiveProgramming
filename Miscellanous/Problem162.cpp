/*
*/

#include <iostream>
#include <cassert>
using namespace std;
unsigned long long pow(int b,int e){
    unsigned long long ans = 1;
    while(e>0){
        ans*=b;
        e-=1;
    }
    return ans;
}
char hexdigit(int i){
    /* i from 0 to 15*/
    assert(i>=0 && i<16);
    switch(i){
        case 0:
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
        case 6:
        case 7:
        case 8:
        case 9:
            return '0'+i; // return the char converted. I am assumming the char set is continuous
        case 10:
            return 'A';
        case 11:
            return 'B';
        case 12:
            return 'C';
        case 13:
            return 'D';
        case 14:
            return 'E';
        case 15:
            return 'F';
        default:
            return 'z'; // error.
    }
}
string hex(unsigned long long n){
    char ans[65];
    ans[64]='\0';
    int bit = 63;
    while(n>0){
        ans[bit]=hexdigit(n%16);
        n/=16;
        bit-=1;
    }
    while (bit>=0){
        ans[bit]=' ';
        bit-=1;
    }
    return string(ans);
}
int main(){
    unsigned long long sum;
    //int n;
    //cin>>n;
    for(int n=1;n<17;n++){
        sum+=(15*pow(16,(n-1))-43*pow(15,(n-1))+41*pow(14,(n-1))-pow(13,n));
    }
    cout<<sum<<" "<<hex(sum)<<endl;
    return 0;
}