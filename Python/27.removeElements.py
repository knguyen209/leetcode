from typing import List

"""
https://leetcode.com/problems/remove-element
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 1 and nums[0] == val:
            nums.pop()
            return 0
        
        start = 0
        end = len(nums) - 1
        count = 0
        
        while start < end:
            if nums[start] == val:
                nums[start], nums[end] = nums[end], nums[start]
                nums.pop()
                end -= 1
            else:
                start += 1
        
        for num in nums:
            if num != val:
                count += 1

        return count

nums = [3,2,2,3]
val = 3
result = Solution().removeElement(nums, val)
print(result)

nums = [0,1,2,2,3,0,4,2]
val = 2
result = Solution().removeElement(nums, val)
print(result)

nums = [1]
val = 1
result = Solution().removeElement(nums, val)
print(result)

nums = [2]
val = 3
result = Solution().removeElement(nums, val)
print(result)