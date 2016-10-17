/*Week of Code 24 - https://www.hackerrank.com/contests/w24/challenges/happy-ladybugs . 
Yeah, I know.. some crappy function names*/

#include <iostream>
#include <unordered_map>
#include <string>
#include <algorithm>

using namespace std;

string canLadyBugHappy(string s);
string ladyBugHappy(string s);

int main(){
    int Q;
    cin>>Q;
    for(int i=0;i<Q;i++){
        int n;
        cin>>n;
        string b;
        cin>>b;
        cout<<canLadyBugHappy(b)<<endl;
    } 

    //testing for_each
    string b="fdg";
    //for_each(b.begin(),b.end(),[](char c){cout<<c<<" ";});
}

string ladyBugHappy(string s){
    if(s.size()==1){
        return "NO";
    }
    char prev = s[0];
    int count = 1;
    for(int i =1;i<s.size();i++){
        if(prev!=s[i]){
            if(count==1) return "NO";
            count=0;
        }
        prev = s[i];
        count+=1;
    }
    return "YES";
}

string canLadyBugHappy(string s){
    int characters[26]={0,0};
    for(int i =0;i<s.size();i++){
        if (s[i]!='_')  characters[s[i]-'A']+=1;
    }
    for(int i=0;i<s.size();i++){
        if (characters[s[i]-'A']==1){
            return "NO";
        }
    }
    if (s.find('_')!=string::npos){
        return "YES";
    }
    else{
        return ladyBugHappy(s);
    }
}