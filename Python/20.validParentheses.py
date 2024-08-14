"""
https://leetcode.com/problems/valid-parentheses
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = ['(', '[', '{']
        closes = [')', ']', '}']
        

        for c in s:
            if c in opens:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                
                last = stack[-1]
                
                if c == ')':
                    if last == '(':
                        stack.pop()
                    else:
                        return False
                
                if c == ']':
                    if last == '[':
                        stack.pop()
                    else:
                        return False
                
                if c == '}':
                    if last == '{':
                        stack.pop()
                    else:
                        return False
                                
        return len(stack) == 0
     

print(Solution().isValid("((()))"))
print(Solution().isValid("()"))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("(]"))
print(Solution().isValid("([)"))