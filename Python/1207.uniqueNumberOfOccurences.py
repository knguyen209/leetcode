from typing import List

"""
https://leetcode.com/problems/unique-number-of-occurrences/

Difficulty: Easy
"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        frequencies = Counter(arr)
        flags = [False for _ in range(len(arr))]
        
        for freq in frequencies:
            if flags[frequencies[freq] - 1]:
                return False
            else:
                flags[frequencies[freq] - 1] = True

        return True
    
print(Solution().uniqueOccurrences([1,2,2,1,1,3])) # True
print(Solution().uniqueOccurrences([1,2])) # False
print(Solution().uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])) # True
