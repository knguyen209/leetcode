'''
https://leetcode.com/problems/find-the-middle-index-in-array/description/
'''

from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        midIndex = -1
        for i in range(0, len(nums)):
            leftArr = nums[0:i]
            leftSum = sum(leftArr)
            rightArr = nums[i+1:len(nums)]
            rightSum = sum(rightArr)
            if leftSum == rightSum:
                return i
            
        return midIndex
        

nums = [2,3,-1,8,4]
result = Solution().findMiddleIndex(nums)
print(result)

nums = [1,-1,4]
result = Solution().findMiddleIndex(nums)
print(result)

nums = [2,5]
result = Solution().findMiddleIndex(nums)
print(result)