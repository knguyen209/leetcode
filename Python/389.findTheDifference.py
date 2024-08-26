"""
https://leetcode.com/problems/find-the-difference/

Difficulty: Easy
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        i = 0
        arr_s = [c for c in s]
        arr_s.sort()

        arr_t = [c for c in t]
        arr_t.sort()
        
        while i < len(s):
            if arr_s[i] != arr_t[i]:
                return arr_t[i]
            i += 1
            
        return arr_t[-1]
    
print(Solution().findTheDifference('abcd', 'abcde'))
# Expected: 'e'

print(Solution().findTheDifference('', 'y'))
# Expected: 'y'

print(Solution().findTheDifference('ae', 'aea'))
# Expected: 'a'
