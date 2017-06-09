#include <iostream>
#include <vector>
using namespace std;
int solution(vector<int> &A){
    int res = 0;
    for(int i=0;i<A.size();i++){
        res^=A[i];
    }
    return res;
}

int main(){
    //int arr[] = {1,2,1,4,2};
    vector<int> A ={1,2,1,4,2} ;//(arr, arr + sizeof(arr) / sizeof(arr[0]) );
    cout<<solution(A);

}