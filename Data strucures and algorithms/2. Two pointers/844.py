"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""

"""
Intuition:
Go through the strings in reverse. Once you find a backspace, add to a backspace counter. Keep on reversing till the backspace counter = 0. Do this for both strings. If we reach a point where the pointers do not equal each other, return false.
If both of the pointers = -1, return True."""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        spointer, tpointer = len(s) -1, len(t) -1
        backs, backt = 0,0
        while True:
            while spointer>=0 and (s[spointer] == '#' or backs):
                if s[spointer] == '#':
                    backs +=1
                else:
                    backs-=1
                spointer-=1
            while tpointer>= 0 and (t[tpointer] == '#' or backt):
                if t[tpointer] == '#':
                    backt +=1
                else:
                    backt-=1
                tpointer-=1
            
            if tpointer<0 or spointer <0 or s[spointer] != t[tpointer]:
                return tpointer == spointer == -1
            tpointer-=1
            spointer-=1

s = Solution()
print(s.backspaceCompare(s = "ab#c", t = "ad#c"))