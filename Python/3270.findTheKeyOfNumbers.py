"""
https://leetcode.com/problems/find-the-key-of-the-numbers/
Difficulty: Easy
"""
class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        answer = 0

        base = 3

        while base >= 0:
            answer += min(num1 // 10**base, num2 // 10**base, num3 // 10**base) * 10**base
            num1 %= 10** base
            num2 %= 10** base
            num3 %= 10** base
            base -= 1

        return answer
    
print(Solution().generateKey(1, 10, 100))
print(Solution().generateKey(987, 879, 798))

# print(789 % 1000)