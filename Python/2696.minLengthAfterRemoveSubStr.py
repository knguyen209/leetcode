"""
https://leetcode.com/problems/minimum-string-length-after-removing-substrings

Difficulty: Easy
"""

class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        
        for c in s:
            if len(stack) > 0:
                if stack[-1] == "A" and c == "B":
                    stack.pop()
                elif stack[-1] == "C" and c == "D":
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)

        answer = "".join(stack)
        return len(answer)
    
print(Solution().minLength("ABFCACDB")) # Output: 2
print(Solution().minLength("ACBBD")) # Output: 5