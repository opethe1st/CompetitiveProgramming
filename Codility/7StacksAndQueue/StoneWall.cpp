#include <iostream>
#include <vector>
#include <stack>
using namespace std;
int solution(vector<int> &H){
    int cuts = 0;
    stack<int> s;
    for(unsigned int i=0; i<H.size();i++){
        int h = H[i];
        while(!s.empty() && s.top()> h){
            s.pop();
        }
        if(s.empty() || s.top()< h){
            s.push(h);
            cuts++;
        }
    }
    return cuts;
}