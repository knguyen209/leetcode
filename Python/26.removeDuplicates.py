from typing import List

"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        curr = nums[0]
        duplicateIndexes = []

        for i in range(1, len(nums)):
            if nums[i] == curr:
                duplicateIndexes.append(i)
            else:
                curr = nums[i]

        
        while len(duplicateIndexes) > 0:
            duplicateIndex = duplicateIndexes.pop()
            nums.pop(duplicateIndex)
        
        return len(nums)

nums = [1,1,2]
result = Solution().removeDuplicates(nums)
print(result) # 2, nums = [1,2,_]

nums = [0,0,1,1,1,2,2,3,3,4]
result = Solution().removeDuplicates(nums)
print(result) # 5, nums = [0,1,2,3,4,_,_,_,_,_]

nums = [1]
result = Solution().removeDuplicates(nums)
print(result) # 5, nums = [0,1,2,3,4,_,_,_,_,_]

