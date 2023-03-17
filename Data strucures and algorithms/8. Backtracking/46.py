"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order."""

"""
Intuition:
We will do a dfs through the list. We will have a current list that stores all of the current values of the recursion. Once we the length of the current list equals the length of the orignal nums list, we know the permuation is complete and 
we can add it to the solution list. In the backtracking for loop, we want to make sure the value we recurse through is not already in the cur.
"""

class Solution:
    def permute(self, nums):
        sol = []
        def backtrack(i, cur):
            if len(cur) == len(nums):
                sol.append(cur[:])
                return
            for j in range(len(nums)):
                if nums[j] not in cur:
                    cur.append(nums[j])
                    backtrack(j+1, cur)
                    del cur[-1]
        backtrack(0, [])
        return sol

s = Solution()
s.permute([1,2,3])