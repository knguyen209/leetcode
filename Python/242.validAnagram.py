"""
https://leetcode.com/problems/valid-anagram
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        dict = Counter(s)

        for i in range(0, len(t)):
            if t[i] in dict:
                dict[t[i]] -= 1
                if dict[t[i]] < 0:
                    return False
            else:
                return False
        
        return True
    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_arr = [c for c in s]
        t_arr = [c for c in t]
        s_arr.sort()
        t_arr.sort()
        
        return ''.join(s_arr) == ''.join(t_arr)
    
s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t)) # True

s = "rat"
t = "car"
print(Solution().isAnagram(s, t)) # False

print(Solution().isAnagram("ab", "a")) # False

print(Solution().isAnagram("aacc", "ccac")) # False