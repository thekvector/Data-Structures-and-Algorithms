/*
On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.
Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly k moves or has moved off the chessboard.

Return the probability that the knight remains on the board after it has stopped moving.
*/

/*
Intuition:
We have to check whether a knight is staying inbounds at a certain spot between eight different directions it can go. Store those directions. Traverse through a grid with the knight going the 8 different directions. If it is out of bounds it will return 0. 
Out of the eight direcions we will recieve a value between 0 and 8 after traversing through. Return that number divided by 8 to get our probability.
*/
#include <vector>
using namespace std;
class Solution {
public:
    double solve(int n,int k, int i, int j, vector<vector<int>>& moves,vector<vector<vector<double>>>& dp){
        if (i<0 || i>=n || j<0 || j>=n) return 0;
        if(k == 0) return 1.0;
        if (dp[i][j][k] != -1) return dp[i][j][k];
        double sol = 0.0;
        for (int x = 0; x<8; x++){
            sol += solve(n,k-1,i+moves[x][0], j + moves[x][1], moves,dp);
        }
        return dp[i][j][k] = sol/8.0;
    }
    double knightProbability(int n, int k, int row, int column) {
        vector<vector<vector<double>>> dp(n,vector<vector<double>>(n,vector<double>(k+1,-1.0)));
        vector<vector<int>> moves{
            {2,1},{1,2},{2,-1},{1,-2},{-2,1},{-1,2},{-2,-1},{-1,-2}
        };
        return solve(n,k,row,column,moves,dp);
        
    }
};

int main(){
    Solution s;
    s.knightProbability(3, 2, 0, 0);
}