"""
https://leetcode.com/problems/ransom-note
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        magazine_counter = Counter(magazine)
        ransom_counter = Counter(ransomNote)

        for key in ransom_counter.keys():
            if key in magazine_counter:
                if magazine_counter[key] < ransom_counter[key]:
                    return False
            else:
                return False
        
        return True
    
ransomNote = "aa"
magazine = "aab"
print(Solution().canConstruct(ransomNote, magazine)) # True

ransomNote = "aa"
magazine = "ab"
print(Solution().canConstruct(ransomNote, magazine)) # False

ransomNote = "a"
magazine = "b"
print(Solution().canConstruct(ransomNote, magazine)) # False