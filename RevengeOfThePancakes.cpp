#include <iostream>
#include <string>
using namespace std;
int countFlip(string s){
    if(s.size()==1 && s[0]=='+'){
        return 0;
    }else if(s.size()==1 && s[0]=='+'){
        return 1;
    }
    int count = 0;
    char prev = s[0];
    for(int i = 1;i<s.size();i++){
        if(prev!=s[i]){
            count+=1;
        }
        prev = s[i];
    }
    if (s[s.size()-1]=='+'){
        return count;
    }else{
        return count+1;
    }
}

int main(int argv,char* arg[]){
    int num;
    string m;
    cin>>num;
    for(int i=1;i<num+1;i++){
        cin>>m;
        cout<<"Case #"<<i<<":"<<" "<<countFlip(m)<<endl;
        
    }
}