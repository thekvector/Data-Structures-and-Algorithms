"""Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""
"""
Intuition:
Traverse the matrix completely first and add to a hashmap all the indices of the letters that exist in the word we are looking for. If the length of the hashmap is less than the length of letters in the word we know it doesn't exist.
Then do a dfs on the matrix using the beginning index of the letter we found in the hashmap.
"""

from collections import defaultdict

class Solution:
    def exist(self, board, word: str) -> bool:
        hm = defaultdict(set)
        m,n = len(board), len(board[0])
        s = set(word)
        for i in range(m):
            for j in range(n):
                if board[i][j] in s:
                    hm[board[i][j]].add((i,j))
        if len(s) != len(hm):
            return False
        if len(hm[word[0]]) > len(hm[word[-1]]):
            word = "".join(reversed(word))
        
        def dfs(wordindex, i,j):
            if wordindex == len(word)-1:
                return True
            hm[word[wordindex]].remove((i,j))
            i_ = [1,-1,0,0]
            j_ = [0,0,1,-1]
            for k in range(4):
                check = (i+i_[k], j+j_[k])
                if check in hm[word[wordindex+1]]:
                    if dfs(wordindex+1,check[0],check[1]):
                        return True
            hm[word[wordindex]].add((i,j))
            return False

        for i,j in hm[word[0]]:
            if dfs(0,i,j):
                return True
        return False

s = Solution()
print(s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))