"""
https://leetcode.com/problems/move-zeroes/description/

Difficulty: Easy
"""
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        num_ptr = 0
        zero_ptr = 0
        n = len(nums)

        while num_ptr < n:
            if zero_ptr < n and nums[zero_ptr] != 0:
                zero_ptr += 1

            if zero_ptr < num_ptr and num_ptr < n and zero_ptr < n and nums[zero_ptr] == 0 and nums[num_ptr] != 0:
                nums[zero_ptr], nums[num_ptr] = nums[num_ptr], nums[zero_ptr]
                zero_ptr += 1
                
            num_ptr += 1



print(Solution().moveZeroes([0,1,0,3,12]))
print(Solution().moveZeroes([0]))
print(Solution().moveZeroes([0, 0]))
print(Solution().moveZeroes([1, 2, 0, 0, 0]))
print(Solution().moveZeroes([1, 0]))
print(Solution().moveZeroes([2, 1]))