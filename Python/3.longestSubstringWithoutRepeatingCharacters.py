"""
https://leetcode.com/problems/longest-substring-without-repeating-characters

Difficulty: Medium
"""
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        map = set()
        maxLen = 0
        i = 0
        j = 0

        while i < len(s):
            if s[i] not in map:
                map.add(s[i])
                i += 1
            else:
                maxLen = max(maxLen, len(map))
                map.remove(s[j])
                j += 1
        
        maxLen = max(maxLen, len(map))
        return maxLen
    
print(Solution().lengthOfLongestSubstring("abcabcbb")) # 3
print(Solution().lengthOfLongestSubstring("bbbbb")) # 1
print(Solution().lengthOfLongestSubstring("pwwkew")) # 3
print(Solution().lengthOfLongestSubstring("c")) # 1
print(Solution().lengthOfLongestSubstring(" ")) # 1
print(Solution().lengthOfLongestSubstring("dvdf")) # 3