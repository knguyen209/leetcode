from typing import List

"""
https://leetcode.com/problems/rotate-array

Difficulty: Medium

"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        while k > 0:
            last = nums.pop()
            nums.insert(0, last)
            k -= 1

        print(nums)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = (len(nums) - k) % len(nums)
        arr = nums[:k]
        nums[:] = nums[k:] + arr


nums = [1,2,3,4,5,6,7]
k = 3
Solution().rotate(nums, k)
# Expected: [5,6,7,1,2,3,4]

nums = [-1,-100,3,99]
k = 2
Solution().rotate(nums, k)
# Expected: [3,99,-1,-100]