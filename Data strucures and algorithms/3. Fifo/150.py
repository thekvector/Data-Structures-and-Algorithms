"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""

"""
Intuition:
Create a stack. Traverse through the tokens in the list. If the token is a number, push into the stack. If the token is an operator, pop the last two elements from the stack and do the operation on the two numbers.
"""

class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for t in tokens:
            
            if t == '+' or t == '-' or t == '/' or t == '*':
                n2 = stack.pop()
                n1 = stack.pop()
                if t == '+':
                    stack.append(n1+n2)
                if t == '-':
                    stack.append(n1-n2)
                if t == '*':
                    stack.append(n1*n2)
                if t == '/':
                    stack.append(int(n1/n2))
            else:
                stack.append(int(t))
        return stack[0]

s = Solution()
s.evalRPN(tokens = ["2","1","+","3","*"])