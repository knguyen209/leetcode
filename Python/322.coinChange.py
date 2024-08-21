"""
https://leetcode.com/problems/coin-change

Difficulty: Medium
"""

from typing import List

import itertools
import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins.sort()
        
        answer = sys.maxsize

        permutations = list(itertools.permutations([1, 2, 3]))

        for permutations in permutations:
            noCoins = self.getMinNumberOfCoins(permutations, amount)
            print(noCoins)
            if noCoins > 0:
                answer = min(answer, noCoins)

        return answer

        # while len(coins) > 0:
        #     coin = coins.pop()
        #     answer += amount // coin
        #     amount = amount % coin    

        # if amount == 0:
        #     return answer
        
        # return -1
    
    def getMinNumberOfCoins(self, coins: tuple[int], amount: int) -> int:
        i = len(coins) - 1
        answer = 0
        while i >= 0:
            coin = coins[i]
            answer += amount // coin
            amount = amount % coin    
            i -= 1

        if amount == 0:
            return answer
        
        return -1

    
    
# coins = [1,2,5]
# amount = 11

# print(Solution().coinChange(coins, amount)) 
# # Expected: 3
# # 5, 5, 1

# print(Solution().coinChange([2], 3))
# # Expected: -1

# print(Solution().coinChange([1], 0))
# # Expected: 0

# print(Solution().coinChange([2,5,10,1], 27))
# # Expected: -1

print(Solution().coinChange([186,419,83,408], 6249))
# Expected: -1 14 * 419 + 2 * 186 

# pers = list(itertools.permutations([1, 2, 3]))
# print(pers)