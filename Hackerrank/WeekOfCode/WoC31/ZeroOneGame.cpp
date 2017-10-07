#include <iostream>

using namespace std;

bool solution(vector<int> v){
    if (v.size()<3){
        return false;
    }else{
        for(int i=2;i<v.size();i++){
            if (s[i-2]==0 and s[i]==0){
                news = s[:i-1]+s[i:];
                return not(solution(news));
            }
        }
        return false;
    }
}

int main(){
    int g;
    cin >> g;
    for(int a0 = 0; a0 < g; a0++){
        int n;
        cin >> n;
        vector<int> sequence(n);
        for(int sequence_i = 0; sequence_i < n; sequence_i++){
           cin >> sequence[sequence_i];
        }
        // If Alice wins, print 'Alice' on a new line; otherwise, print 'Bob'
        if (solution(sequence)){
            cout<<"Bob"<<endl;
        }else{
            cout<<"Alice"<<endl;
        }
    }
    return 0;
}