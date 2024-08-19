from typing import List

"""
https://leetcode.com/problems/group-anagrams/

Difficulty: Medium
"""
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        map = defaultdict(list)

        for str in strs:
            sorted_word = ''.join(sorted(str))
            map[sorted_word].append(str)

        return list(map.values())
    
strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))
# Expected: [["bat"],["nat","tan"],["ate","eat","tea"]]