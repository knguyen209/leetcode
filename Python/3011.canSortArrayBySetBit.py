"""
https://leetcode.com/problems/find-if-array-can-be-sorted

Difficulty: Medium
"""

from typing import List
    
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def getNumSetBits(num: int):
            return bin(num).count("1")
        
        segments = []
        currSegment = [nums[0]]
        currSetBit = getNumSetBits(nums[0])

        for i in range(1, len(nums)):
            setBit = getNumSetBits(nums[i])
            
            if currSetBit == setBit:
                currSegment.append(nums[i])
            else:
                segments.append(currSegment)
                currSegment = [nums[i]]
                currSetBit = setBit

            if i == len(nums) - 1:
                segments.append(currSegment)

        for i in range(1, len(segments)):
            if max(segments[i - 1]) > min(segments[i]):
                return False
        
        return True

    
print(Solution().canSortArray([8,4,2,30,15])) # True
print(Solution().canSortArray([1,2,3,4,5])) # True
print(Solution().canSortArray([3,16,8,4,2])) # False
print(Solution().canSortArray([20,16])) # False
print(Solution().canSortArray([75,34,30])) # False
