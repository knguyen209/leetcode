from typing import List

"""
https://leetcode.com/problems/majority-element
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
"""

# Approach #1: Time and Space Complexity O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        major = nums[0]
        majorCount = 1
        for num in nums:
            if dict.get(num):
                dict[num] = dict[num] + 1
            else:
                dict[num] = 1

            if majorCount < dict[num]:
                major = num
                majorCount = dict[num]
        
        return major
        
# Approach #2:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter

        count = Counter(nums)
        
        return max(count, key=count.get)

# Approach #3:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate

nums = [3,2,3]
print(Solution().majorityElement(nums)) # Expect 3

nums = [2,2,1,1,1,2,2]
print(Solution().majorityElement(nums)) # Expect 2