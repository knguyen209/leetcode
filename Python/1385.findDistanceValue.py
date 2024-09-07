"""
https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

Difficulty: Easy
"""
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        answer = 0

        for i in range(len(arr1)):
            count = 0
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    break
                count += 1
            if count == len(arr2):
                answer += 1
            
        return answer
    
arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
print(Solution().findTheDistanceValue(arr1, arr2, d)) # Expected: 2

arr1 = [1,4,2,3]
arr2 = [-4,-3,6,10,20,30]
d = 3
print(Solution().findTheDistanceValue(arr1, arr2, d)) # Expected: 2