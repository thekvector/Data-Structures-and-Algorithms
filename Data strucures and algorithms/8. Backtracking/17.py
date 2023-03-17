"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

"""
Intuition:
First we create a dictionary of the numbers and the respective letters. Thenf or every number in the digits variable that was passed, we pass it through a backtracking for loop until the length of the recursion equals the length of the digits. We then add the
recursion into the solution and backtrack."""

class Solution:
    def letterCombinations(self, digits: str):
        sol = []
        if digits == '':
            return sol
        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        def bt(i, cur=""):
            if len(cur) == len(digits):
                sol.append(cur[:])
                return
            
            for letter in m[digits[i]]:
                bt(i+1, cur+ letter)
                    
        bt(0)
        return sol

s = Solution()
s.letterCombinations('23')
