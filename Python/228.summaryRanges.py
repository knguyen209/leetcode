from typing import List

'''
https://leetcode.com/problems/summary-ranges/
'''

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [str(nums[0])]
        
        ranges = []
        start = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] + 1:
                if start == nums[i - 1]:
                    ranges.append(f"{start}")
                else:
                    ranges.append(f"{start}->{nums[i-1]}")
                start = nums[i]
            if i == len(nums) - 1:
                if start == nums[i]:
                    ranges.append(f"{start}")
                else:
                    ranges.append(f"{start}->{nums[i]}")

        return ranges
    
nums = [0,1,2,4,5,7]
print(Solution().summaryRanges(nums))
# Expect: ["0->2","4->5","7"]

nums = [0,2,3,4,6,8,9]
print(Solution().summaryRanges(nums))
# Expect: ["0","2->4","6","8->9"]