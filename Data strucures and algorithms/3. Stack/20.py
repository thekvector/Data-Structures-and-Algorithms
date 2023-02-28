"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

"""
Intuition:
Traverse through the string. Add open brackets into a stack. If we reach a closed bracket, pop an element from the stack. If the stack is empty know the brackets aren't valid. If the popped bracket isn't the same type as the closed bracket,
we know the brackets aren't valid.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(', '[', '{'}
        for char in s:
            if char in dic:
                stack.append(char)
            elif char == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif char == ']':
                if not stack or stack.pop() != '[':
                    return False
            elif char == '}':
                if not stack or stack.pop() != '{':
                    return False
        return len(stack) == 0


s= Solution()
print(s.isValid("()[]{}"))