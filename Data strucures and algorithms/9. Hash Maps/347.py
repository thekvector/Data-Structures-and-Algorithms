#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

#Intuition:
#Use bucket sort but with indices

from collections import Counter

class Solution:
    def topKFrequent(self, nums, k: int) :
        n = len(nums)
        bucket = [set() for i in range(n+1)]
        c = Counter(nums)
        for key, value in c.items():
            bucket[value].add(key)
        sol = []
        for i in range(n,-1,-1):
            if bucket[i]:
                for val in bucket[i]:
                    sol.append(val)
                    k-=1
                    if k== 0:
                        return sol

s = Solution()
print(s.topKFrequent(nums = [1,1,1,2,2,3], k = 2))