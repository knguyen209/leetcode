from typing import List

"""
https://leetcode.com/problems/largest-number/
Difficulty: Medium
"""

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert integers to strings
        array = list(map(str, nums))
        
        # Custom sorting with a lambda function
        array.sort(key=lambda x: x*10, reverse=True)
        print(array)
        
        # Handle the case where the largest number is "0"
        if array[0] == "0":
            return "0"
        
        # Build the largest number from the sorted array
        largest = ''.join(array)
        
        return largest

    
# print(Solution().largestNumber([10,2])) # "210"
print(Solution().largestNumber([3,30,34,5,9, 978, 98, 95])) # "9534330"
print(Solution().largestNumber([3,30,34,5,9])) # "9534330"