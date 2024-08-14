"""
https://leetcode.com/problems/isomorphic-strings
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        mapped_values = []
        for i in range(0, len(s)):
            if s[i] not in map:
                if t[i] not in mapped_values:
                    map[s[i]] = t[i]
                    mapped_values.append(t[i])
                else:
                    return False
            else:
                if map[s[i]] != t[i]:
                    return False

        return True
    
s = "egg"
t = "add"
print(Solution().isIsomorphic(s, t)) # True

s = "foo"
t = "bar"
print(Solution().isIsomorphic(s, t)) # False

s = "paper"
t = "title"
print(Solution().isIsomorphic(s, t)) # True

s = "badc"
t = "baba"
print(Solution().isIsomorphic(s, t)) # False