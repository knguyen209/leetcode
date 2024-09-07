from typing import List

"""
https://leetcode.com/problems/can-place-flowers

Difficulty :Easy
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        for i in range(len(flowerbed)):
            if n > 0:
                if i == 0 and i + 1 < len(flowerbed):
                    if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        n -=1

                if i - 1 > 0 and i + 1 < len(flowerbed):
                    if flowerbed[i] == 0 and flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0:
                        flowerbed[i] = 1
                        n -= 1

                if i == len(flowerbed) - 1:
                    if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                        flowerbed[i] = 1
                        n -= 1

        print(flowerbed)

        return n == 0
    
flowerbed = [1,0,0,0,1]
n = 1
print(Solution().canPlaceFlowers(flowerbed, n)) # True

flowerbed = [1,0,0,0,1]
n = 2
print(Solution().canPlaceFlowers(flowerbed, n)) # False

flowerbed = [0,0,1,0,1]
n = 1
print(Solution().canPlaceFlowers(flowerbed, n)) # True

flowerbed = [1,0,0,0,1,0,0]
n = 2
print(Solution().canPlaceFlowers(flowerbed, n)) # True