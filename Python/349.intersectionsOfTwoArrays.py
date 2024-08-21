from typing import List

"""
https://leetcode.com/problems/intersection-of-two-arrays/

Difficulty: Easy
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)        
        return list(set1.intersection(set2))
    
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersects = []

        if len(nums1) <= len(nums2):
            small_list = nums1
            large_list = nums2
        else:
            small_list = nums2
            large_list = nums1

        for i in range(len(small_list)):
            if small_list[i] in large_list and small_list[i] not in intersects:
                intersects.append(small_list[i])

        return intersects
    
nums1 = [1,2,2,1]
nums2 = [2,2]
print(Solution().intersection(nums1, nums2))