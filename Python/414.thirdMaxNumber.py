from typing import List

"""
https://leetcode.com/problems/third-maximum-number/

Return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.
Difficulty: Easy
"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        my_set = set(nums)
        my_arr = list(my_set)
        my_arr.sort()
        return my_arr[-3] if len(my_arr) >= 3 else my_arr[-1]
    
print(Solution().thirdMax([1,2,3])) # Expected: 1
print(Solution().thirdMax([1,2])) # Expected: 2
print(Solution().thirdMax([2,2,3,1])) # Expected: 1