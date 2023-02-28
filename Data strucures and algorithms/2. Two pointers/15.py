"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

"""
Intuition:
We are going to be using three pointers. The first pointer is going to iterate through every element in the list except the last two. Do a nested loop at every iteration where we have two pointers now that point to the first pointer index + 1 and the back index.
Iterate through the two pointers till the sum of all three pointers equals 0."""

class Solution:
    def threeSum(self, nums):
        nums.sort()
        sol = []
        for num1 in range(len(nums)-2):
            if num1>0 and nums[num1] == nums[num1-1]:
                continue
            num2, num3 = num1+1, len(nums) -1 

            while num2< num3:
                check = nums[num1] + nums[num2] + nums[num3]
                if check == 0:
                    sol.append([nums[num1], nums[num2], nums[num3]])
                    while num2 < num3 and  nums[num2] == nums[num2+1]:
                        num2+=1
                    num2+=1
                    while num3 > num2 and  nums[num3] == nums[num3-1]:
                        num3-=1
                    num3-=1
                elif check<0:
                    num2+=1
                elif check>0:
                    num3-=1
            
        return sol

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))