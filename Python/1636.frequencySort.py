"""
https://leetcode.com/problems/sort-array-by-increasing-frequency/

Difficulty: Easy
"""
from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
        freq = Counter(nums)
        tuples = []
        
        for i in freq:
            tuples.append((freq[i], i))

        def custom_sort(a, b):
            if a[0] < b[0]:
                return -1
            elif a[0] == b[0]:
                if a[1] > b[1]:
                    return -1
                else:
                    return 1
            else:
                return 1
            
        from functools import cmp_to_key
        letter_cmp_key = cmp_to_key(custom_sort)

        tuples.sort(key=letter_cmp_key)

        answer = []
        for tuple in tuples:
            for i in range(tuple[0]):
                answer.append(tuple[1])        

        return answer
    

    
print(Solution().frequencySort([1,1,2,2,2,3]))
print(Solution().frequencySort([2,3,1,3,2]))
print(Solution().frequencySort([-1,1,-6,4,5,-6,1,4,1]))