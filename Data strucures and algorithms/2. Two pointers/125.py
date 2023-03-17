"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

"""

"""
Intuition:
Have one pointer pointing to front of string and one pointing at back. Check if both are equal. If not, return false. Else, keep on going till both the pointers equal each other. Return True"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1, p2 = 0,len(s) -1 

        while p1<p2:
            if not s[p1].isalpha() and not s[p1].isnumeric(): 
                p1+=1
                continue
            if not s[p2].isalpha() and not s[p2].isnumeric(): 
                p2 -=1
                continue
            if s[p1].lower() != s[p2].lower(): return False
            p1+=1
            p2-=1
        return True

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))