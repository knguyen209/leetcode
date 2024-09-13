from typing import List

"""
https://leetcode.com/problems/split-the-array/
Difficulty: Easy
"""
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        from collections import Counter
        map = Counter(nums)

        for i in map:
            if map[i] > 2:
                return False
            
        return True

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        nums.sort()
        count = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 0:
                count += 1
                if count > 2:
                    return False
            else:
                count = 1
        return True

print(Solution().isPossibleToSplit([1,1,2,2,3,4])) # True, [1,2,3], [1,2,4]
print(Solution().isPossibleToSplit([1,1,1,1])) # False
