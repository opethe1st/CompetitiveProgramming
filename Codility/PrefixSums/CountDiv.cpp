int solution(int A, int B, int K) {
    // write your code in C++14 (g++ 6.2.0
    int first = A+(K-A%K)%K;
    int last = B-B%K;
    //cout<<first<<" "<<last<<endl;
    if (last<first){
        return 0;
    }
    else{
        return (last-first)/K+1;
    
    }
}