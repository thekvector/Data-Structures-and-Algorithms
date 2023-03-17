"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

"""
Intuition:
Iterate through the list and sort all of the words and add to a hashmap. Make the sorted word the key and append to it the original word. Create a solution list using the all of the lists made in the hashmap."""

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        hm = defaultdict(list)
        for word in strs:
            check = word
            check = "".join(sorted(check))
            hm[check].append(word)
        sol = []
        for _, l in hm.items():
            sol.append(l)
        return sol

s = Solution()
print(s.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))