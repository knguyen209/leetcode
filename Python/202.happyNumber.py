# https://leetcode.com/problems/happy-number
class Solution:
    def isHappy(self, n: int) -> bool:
        while len(str(n)) > 1:
            n = self.squaredSum(n)
        
        if n == 1 or n == 7:
            return True
        
        return n == 1

    def squaredSum(self, n: int) -> int:        
        sum = 0
        for x in str(n):
            sum += int(x)**2
        return sum
    
print(Solution().isHappy(19))
print(Solution().isHappy(2))
print(Solution().isHappy(7))
print(Solution().isHappy(1111111))