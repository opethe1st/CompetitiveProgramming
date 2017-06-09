int solution(vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)
    int l = A.size();
    long sumFirstN = (l+1)*(l+2)/2;
    long s=0;
    for(int i=0;i<l;i++){
        s+=A[i];
    }
    return sumFirstN-s;
}