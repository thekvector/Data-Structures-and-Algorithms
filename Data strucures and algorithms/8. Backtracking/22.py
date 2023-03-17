"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""
"""
Intuition:
We will have a variable open and closed that tracks the number of open and closed parentheses currently in the recursion. If open equals closed which equals n, we know the generation is complete and we can add the parentheses into the solution list.
If open is less than n, we continue the backtracking recursion by adding 1 to open. if close is less than open, we add to the closed variable."""

class Solution:
    def generateParenthesis(self, n: int):
        stack = []
        sol = []
        def bt(open, close):
            if open == close == n:
                sol.append("".join(stack))
                return
            if open < n:
                stack.append('(')
                bt(open+1, close)
                stack.pop()
            if close<open:
                stack.append(')')
                bt(open, close+1)
                stack.pop()
        
        bt(0,0)
        return sol

s= Solution()
s.generateParenthesis(3)