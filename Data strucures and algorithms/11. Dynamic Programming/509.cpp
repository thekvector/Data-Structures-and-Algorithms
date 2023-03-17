/*
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 */

/*
Intuition:
So we know at every number n, the fibonacci number is going to be the fibonacci number of n-1 + the fibonaccit number of n-2. Have the fibonacci stored in a dp cache once we have already solved it. Then return the value.*/
#include<vector>
using namespace std;
class Solution {
public:
    int solve(int n, vector<int>& dp){
        if (n<=1) return n;
        return dp[n] = solve(n-1,dp) + solve(n-2,dp);
    }
    int fib(int n) {
        vector<int> dp(n+1, 0);
        return solve(n,dp);
    }
};

int main(){
    Solution s;
    s.fib(6);
}