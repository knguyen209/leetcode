"""
https://leetcode.com/problems/longest-common-prefix

Difficulty: Easy

"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x: len(x))
        
        common_prefix = ''
        
        for i in range(0, len(strs[0])):
            curr = strs[0][i]
            
            for j in range(1, len(strs)):
                if strs[j][i] != curr:
                    return common_prefix
            
            common_prefix += curr

        return common_prefix
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)

        common_prefix = ''
        
        first_str = strs[0]
        last_str = strs[-1]

        for i in range(min(len(first_str), len(last_str))):
            if first_str[i] != last_str[i]:
                return common_prefix
            
            common_prefix += first_str[i]
        
        return common_prefix

print(Solution().longestCommonPrefix(["flower","flow","flight"])) # Expect: "fl"

print(Solution().longestCommonPrefix(["dog","racecar","car"]))

print(Solution().longestCommonPrefix(["abab","aba","abc"]))