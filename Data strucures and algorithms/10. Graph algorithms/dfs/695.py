"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""

"""
Intuition:
We want to go through the grid with dfs. Whenever we find a piece of land when we start the iteration, start the dfs and count how many tiles of land there are by going in all 4 directions. Return the largest island by using
the max function after iterating through the whole grid.
"""
class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>= n or grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            sol = 1
            sol += dfs(i-1,j)
            sol += dfs(i+1,j)
            sol += dfs(i, j-1)
            sol += dfs(i, j+1)
            return sol
        self.sol = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.sol = max(self.sol, dfs(i,j))
        return self.sol

s = Solution()
s.maxAreaOfIsland(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
