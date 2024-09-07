from typing import List

"""
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

Difficulty: Easy
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = []
        for i in range(len(candies)):
            answer.append(False if (candies[i] + extraCandies) < max(candies) else True)

        return answer


candies = [2,3,5,1,3]
extraCandies = 3
print(Solution().kidsWithCandies(candies, extraCandies))

candies = [4,2,1,1,2]
extraCandies = 1
print(Solution().kidsWithCandies(candies, extraCandies))

candies = [12,1,12]
extraCandies = 10
print(Solution().kidsWithCandies(candies, extraCandies))