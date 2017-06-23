#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int solution(vector<int> &A, vector<int> &B){
    int nkilled = 0;
    stack<int> MovingRight;
    for(unsigned int i = 0; i<A.size(); i++){
        if(B[i] == 1){  // Moving right
            MovingRight.push(A[i]);
        }else{
            if(!MovingRight.empty() && MovingRight.top() > A[i]){
                nkilled += 1;
            }else {
                while(!MovingRight.empty() && MovingRight.top() < A[i]){
                    nkilled +=1;
                    MovingRight.pop();
                }
                if(!MovingRight.empty() && MovingRight.top() > A[i]){
                    nkilled += 1;
                }
            }   
        }
    }
    //cout<<nkilled<<endl;
    return A.size()-nkilled;
}

int main(){
    vector<int> A = {4, 3, 2, 1, 1};
    vector<int> B = {0, 0, 1, 1, 0};
    cout<<solution(A, B)<<endl;
}