from typing import List

"""
https://leetcode.com/problems/merge-sorted-array
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i in range(m, m+n):
            nums1[i] = nums2[j]
            j += 1

        nums1.sort()
        print(nums1)
                    

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
sorted_arr = Solution().merge(nums1, m, nums2, n)

nums1 = [0]
m = 0
nums2 = [1]
n = 1
sorted_arr = Solution().merge(nums1, m, nums2, n)

nums1 = [4,0,0,0,0,0]
m = 1
nums2 = [1,2,3,5,6]
n = 5
sorted_arr = Solution().merge(nums1, m, nums2, n)

nums1 = [1,2,4,5,6,0]
m = 5
nums2 = [3]
n = 1
sorted_arr = Solution().merge(nums1, m, nums2, n)

nums1 = [4, 5, 6, 0, 0, 0]
m = 3
nums2 = [1, 2, 3]
n = 3
sorted_arr = Solution().merge(nums1, m, nums2, n)