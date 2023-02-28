"""
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

"""
Intuition:
We will go through every element in the list recursively. During the recursion we will do a for loop through the rest of the array and add the element at the current index until we reach the end.
"""

class Solution:
    def subsets(self, nums):
        sol = [[]]
        def bt(i, cur):
            for j in range(i, len(nums)):
                cur.append(nums[j])
                sol.append(cur[:])
                bt(j+1, cur)
                del cur[-1]
        bt(0, [])
        return sol

s = Solution()
s.subsets(nums = [1,2,3])