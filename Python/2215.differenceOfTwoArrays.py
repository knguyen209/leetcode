from typing import List

"""
https://leetcode.com/problems/find-the-difference-of-two-arrays

Difficulty: Easy
"""

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        answer = []
        answer.append(list(set1.difference(set2)))
        answer.append(list(set2.difference(set1)))
        return answer
    
nums1 = [1,2,3]
nums2 = [2,4,6]
print(Solution().findDifference(nums1, nums2)) # [[1,3],[4,6]]

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(Solution().findDifference(nums1, nums2)) # [[3],[]]