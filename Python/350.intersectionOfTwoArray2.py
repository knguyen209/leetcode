from typing import List

"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Difficulty: Easy
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersects = []

        if len(nums1) <= len(nums2):
            small_list = nums1
            large_list = nums2
        else:
            small_list = nums2
            large_list = nums1

        for i in range(len(small_list)):
            if small_list[i] in large_list:
                intersects.append(small_list[i])
                large_list.remove(small_list[i])

        return intersects
  
nums1 = [1,2,2,1]
nums2 = [2,2]
print(Solution().intersect(nums1, nums2))

nums1 = [3,1,2]
nums2 = [1,1]
print(Solution().intersect(nums1, nums2))