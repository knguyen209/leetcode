from typing import List

"""
https://leetcode.com/problems/find-lucky-integer-in-an-array/

Difficulty: Easy

Given an array of integers arr, a lucky integer is an integer 
that has a frequency in the array equal to its value.
Return the largest lucky integer in the array. 
If there is no lucky integer return -1.
"""

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        frequencies = Counter(arr)
        arr = [num for num in frequencies if frequencies[num] == num]
        arr.sort()

        if len(arr) > 0:
            return arr[-1]
            
        return -1
    
arr = [2,2,3,4]
print(Solution().findLucky(arr))

arr = [1,2,2,3,3,3]
print(Solution().findLucky(arr)) 
# Expected: 3
# 1, 2 and 3 are all lucky numbers, return the largest of them.