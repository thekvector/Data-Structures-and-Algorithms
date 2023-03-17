/*
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
*/

/*
Intuition:
Create a dp cache table. Since we are trying to figure out distinct ways to reach the top, we have to take the amount of stairs and add the total amount of ways we can get down if we either take one step down or two steps down. Return that total.
*/
#include <vector>
using namespace std;
class Solution {
public:
    int solve(int n, vector<int>& dp){
        if (n==0) return 1;
        if (n<0) return 0;
        if (dp[n] != -1) return dp[n];
        return dp[n] = solve(n-1,dp) + solve(n-2,dp);
    }
    int climbStairs(int n) {
        vector<int> dp(n+1,-1);
        return solve(n,dp);
    }
};

int main(){
    Solution s;
    s.climbStairs(4);
}