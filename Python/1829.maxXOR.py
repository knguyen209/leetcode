"""
https://leetcode.com/problems/maximum-xor-for-each-query/

Difficulty: Medium
"""
from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        answers = []
        arr = [0 for _ in range(len(nums))]
        maxPossibleXor = 2**maximumBit - 1
        
        for i in range(len(nums)):
            if i == 0:
                arr[0] = nums[0]
            else:
                arr[i] = arr[i - 1]^nums[i]
        
        while len(arr) > 0:
            k = arr[-1]^maxPossibleXor
            answers.append(k)
            arr.pop()
        
        return answers
    
print(Solution().getMaximumXor([0,1,1,3], maximumBit=2)) # [0,3,2,3]
print(Solution().getMaximumXor([2,3,4,7], maximumBit=3)) # [5, 2, 6, 5]