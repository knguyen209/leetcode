
"""
https://leetcode.com/problems/number-of-beautiful-pairs/
"""

from typing import List

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        import math
        count = 0
        for i in range(len(nums)):
            first = int(str(nums[i])[0])
            for j in range(i, len(nums)):
                last = int(str(nums[j])[-1])
                if i != j and math.gcd(first, last) == 1:
                    print(nums[i], nums[j])
                    count += 1
        return count
    
print(Solution().countBeautifulPairs([2,5,1,4])) # 5
print(Solution().countBeautifulPairs([11,21,12])) # 2