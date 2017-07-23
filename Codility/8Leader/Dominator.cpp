#include <iostream>
#include <vector>
#include <stack>
using namespace std;
int solution(vector<int> &A)
{
    stack<int> s;
    int i = 0;
    while (i < A.size())
    {
        if (s.empty() || s.top() == A[i])
        {
            s.push(A[i]);
        }
        else
        {
            s.pop();
        }

        i++;
    }
    if (s.count() > 1)
    {
        int ans= s.top();
    }
    else
    {
        int ans = -1; // no leader
    }
    return ans
}

int main()
{
}