"""
https://leetcode.com/problems/first-unique-character-in-a-string/

Difficulty: Easy
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        map = Counter(s)
        
        for i in range(len(s)):
            if map[s[i]] == 1:
                return i
            
        return -1
    
print(Solution().firstUniqChar("leetcode")) 
# Expected: 0

print(Solution().firstUniqChar("loveleetcode")) 
# Expected: 2

print(Solution().firstUniqChar("aabb")) 
# Expected: -1
