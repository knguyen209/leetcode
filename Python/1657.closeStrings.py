"""
https://leetcode.com/problems/determine-if-two-strings-are-close/

Difficulty: Medium
"""

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        if set(word1) != set(word2):
            return False
        
        from collections import Counter
        
        arr1 = list(Counter(word1))
        arr2 = list(Counter(word2))
        arr1.sort()
        arr2.sort()
        
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False
        
        return True
    
word1 = "abc"
word2 = "bca"
print(Solution().closeStrings(word1, word2))

word1 = "a"
word2 = "aa"
print(Solution().closeStrings(word1, word2))

word1 = "abbzzca"
word2 = "babzzcz"
print(Solution().closeStrings(word1, word2))
