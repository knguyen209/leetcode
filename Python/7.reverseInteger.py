"""
https://leetcode.com/problems/reverse-integer/

Difficulty: Medium
"""

class Solution:
    def reverse(self, x: int) -> int:        
        is_negative = False

        if x < 0:
            is_negative = True
            x *= -1
        
        stack = []

        while x / 10 > 0:
            stack.append(x % 10)
            x = x // 10

        answer = 0
        base = len(stack) - 1
        
        while base >= 0:
            answer += stack.pop(0) * (10 ** base)
            base -= 1

        answer *= 1 if not is_negative else -1

        if answer < -(2 ** 31) or answer > (2**31 -1):
            return 0

        return answer
    
print(Solution().reverse(123)) # Expected: 321
print(Solution().reverse(-123)) # Expected: -321
print(Solution().reverse(120)) # Expected: 21
print(Solution().reverse(1534236469)) # Expected: 0
