"""
https://leetcode.com/problems/valid-perfect-square/

Difficulty: Easy
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i * i <= num:
            if i * i == num:
                return True
            i += 1

        return False
    
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return (num ** 0.5) % 1 == 0
    
print(Solution().isPerfectSquare(16)) # True
print(Solution().isPerfectSquare(14)) # False
