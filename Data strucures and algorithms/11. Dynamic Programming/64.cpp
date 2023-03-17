/*
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
*/

/*
Intuition:
Since we can only move either down or up, we do a recursion dfs of the grid and for each point in the grid, we check if it's cheaper to reach the end going down or going to the right. We then store the minimum value in a dp table cache so that we don't redo problems
we've already solved and return the min.
*/
#include<vector>
using namespace std;
class Solution {
public:
    int solve(vector<vector<int>>& grid, int i, int j, int m, int n, vector<vector<int>>& dp){
        if (i>=m || j>=n) return 1e9;
        if (dp[i][j] != -1) return dp[i][j];
        if (i== m-1 && j == n-1) return grid[i][j];
        return dp[i][j] = min(solve(grid,i+1,j,m,n,dp), solve(grid, i,j+1,m,n,dp)) + grid[i][j];
    }
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> dp(m,vector<int>(n,-1));
        return solve(grid,0,0,m,n,dp);

    }
};

int main(){
    Solution s;
    vector<vector<int>> grid {{1,3,1},{1,5,1},{4,2,1}};
    s.minPathSum(grid);
}