"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

"""
"""
Intution:
Traverse through the matrix. Whenever you find a 1 which is a piece of land, pass the indices through a dfs algorithm. All of the neighboring pieces of land we should convert to 0. Then we know that this is one island. Coninue on with the traversal.
"""

class Solution:
    def numIslands(self, grid) -> int:
        m,n = len(grid), len(grid[0])
        self.sol = 0
        def dfs(i,j):
            if i<0 or i>= m or j<0 or j>= n or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j)
                    self.sol +=1
        return self.sol


s = Solution()
s.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])