"""
https://leetcode.com/problems/water-bottles

Difficulty: Easy
"""

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        answer = numBottles
        
        while numBottles >= numExchange:
            answer = answer + numBottles // numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange

        return answer
    
print(Solution().numWaterBottles(9, 3)) # 13
print(Solution().numWaterBottles(15, 4)) # 19