/*
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

*/
/*
Intuition:
Create a dp cache and do a dfs through the coins. We can choose to either include the current coin or not include the current coin. Return the minimum between chooding the current coin or not including the current coin recursively.*/
#include <vector>
using namespace std;
class Solution {
public:
    int solve(vector<int>& coins, int i, int amount, int n,vector<vector<int>>& dp){
        if (amount<0|| i == n) return 1e9;
        if (amount == 0) return 0;
        if (dp[i][amount] != -1) return dp[i][amount];
        return dp[i][amount] = min(solve(coins, i,amount-coins[i],n,dp) + 1, solve(coins, i+1,amount,n,dp));
    }
    int coinChange(vector<int>& coins, int amount) {
        int n = coins.size();
        vector<vector<int>> dp(n,vector<int>(amount+1,-1));
        int s = solve(coins,0,amount,n,dp);
        if (s== 1e9) return -1;
        return s;
    }
};

int main(){
    Solution s;
    vector<int> coins {1,2,5};
    s.coinChange(coins, 11);
}