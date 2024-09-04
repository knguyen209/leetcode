"""
https://leetcode.com/problems/powx-n/?envType=study-plan-v2&envId=top-interview-150

Difficulty: Medium
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            x = 1 / x
            n = -n

        answer = 1
        current_product = x

        while n > 0:
            if n % 2 == 1:
                answer *= current_product
                
            current_product *= current_product

            n = n // 2
        
        return answer

    

print(Solution().myPow(1, -2))
print(Solution().myPow(2.10000, 3))
print(Solution().myPow(2.00000, -2))