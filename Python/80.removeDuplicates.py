"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

Difficulty: Medium

"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        count = 1
        duplicates = []

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
                if count >= 3:
                    duplicates.append(nums[i])
            else:
                count = 1

        k = len(nums) - len(duplicates)

        while len(duplicates) > 0:
            num = duplicates[-1]
            nums.remove(num)
            nums.append(num)
            duplicates.pop()

        return k
    
# print(Solution().removeDuplicates([1,1,1,2,2,3]))
# # 5, nums = [1,1,2,2,3,_]

# print(Solution().removeDuplicates([0,0,1,1,1,1,2,3,3]))
# # 7, nums = [0,0,1,1,2,3,3,_,_]

# print(Solution().removeDuplicates([1]))
# # 1, nums = [1]

# print(Solution().removeDuplicates([1,1,1]))
# # 2, nums = [1,1]

print(Solution().removeDuplicates([1,1,1,2,2,2,3,3]))
# 2, nums = [1,1,2,2,3,3]