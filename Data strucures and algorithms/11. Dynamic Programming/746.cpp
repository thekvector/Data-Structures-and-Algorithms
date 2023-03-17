/*You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
*/

/*
Intution:
Create a dp table intializing the first two values of the table with the first two values of the cost table. For every iteration of the cost table, check whether it is cheaper to reach the current step by paying from the last step or second to last step
using the dp cache table. Inser the min into the current index for the dp table. At the end return the minimum between the last or second to last index in the dp table.
*/

#include<vector>
using namespace std;
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        vector<int> dp(n, -1);
        dp[0] = cost[0];
        dp[1] = cost[1];
        for (int i = 2; i<n; i++){
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i];
        }
        return min(dp[n-1],dp[n-2]);
    }
};

int main(){
    Solution s;
    vector<int> cost {10,15,20};
    s.minCostClimbingStairs(cost);
}