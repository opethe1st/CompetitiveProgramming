/* The algorithm, finds the leader from the front and from the back
precomputes these two values in left and right arrays and then
iterates to count the number that are the same
*/
#include <iostream>
#include <vector>
#include <stack>

int solution(vector<int> &A)
{
    vector<int> left;
    vector<int> right;
    stack<int> leftstack;
    stack<int> rightstack;
    int i = 0;
    while (i < A.size())
    {
        if (leftstack.empty() || leftstack.top() == A[i])
        {
            leftstack.push(A[i]);
        }
        else
        {
            leftstack.pop();
        }
        if(leftstack.count() > 1){
            left[i] = leftstack.top();
        }else{
            left[i] = -1;   // no leader
        }
        i++;
    }
    int j = A.size() - 1;
    while (j >= 0)
    {
        if (rightstack.empty() || rightstack.top() == A[j])
        {
            rightstack.push(A[j]);
        }
        else
        {
            rightstack.pop();
        }
        if(rightstack.count()>1){
            right[j] = rightstack.top();
        }else{
            right[j] = -1;  // no leader
        }
        j--;
    }
    int count = 0;
    for (i = 0; i < A.size()-1; i++)
    {
        if (left[i]!=-1 && left[i] == right[i+1]){
            count+=1;
        }
    }
    return count;
}