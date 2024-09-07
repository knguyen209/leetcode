"""
https://leetcode.com/problems/string-to-integer-atoi/description/

Difficulty: Medium
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        is_negative = False
        queue = []

        if len(s) == 0:
            return 0

        if s[0] == '-':
            is_negative = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        for i in range(len(s)):
            if str.isdigit(s[i]):
                queue.append(s[i])
            else:
                break

        if len(queue) > 0:        
            answer = int(''.join(queue))
        else:
            return 0

        answer *= -1 if is_negative else 1
        
        left_bound = -2**31
        right_bound = 2**31 - 1 
        if answer < left_bound:
            return left_bound
        
        if answer > right_bound:
            return right_bound

        return answer
    
print(Solution().myAtoi("42"))              # 42
print(Solution().myAtoi(" -042"))           # -42
print(Solution().myAtoi("1337c0d3"))        # 1337
print(Solution().myAtoi("0-1"))             # 0
print(Solution().myAtoi("words and 987"))   # 0
print(Solution().myAtoi("+12"))             # 12
print(Solution().myAtoi("-+12"))            # 0
