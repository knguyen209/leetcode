from typing import List

"""
https://leetcode.com/problems/count-the-number-of-consistent-strings
Difficulty: Easy
"""

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowed_set = set(list(allowed))
        for word in words:
            word_set = set(list(word))
            if len(word_set - allowed_set) == 0:
                count += 1
        return count
    
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print(Solution().countConsistentStrings(allowed, words))