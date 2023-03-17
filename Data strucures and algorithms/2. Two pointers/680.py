"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

"""

"""
Intuition:
Have two pointers pointing to front and back. When you reach a point where teh front pointer does not equal back, return whether the list exluding the front or back index is a palindrome."""

class Solution:

    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) -1
        count = 0 

        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l+1:r+1] , s[l: r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]

            l = l +1
            r = r - 1

        return True

s = Solution()
print(s.validPalindrome("abca"))