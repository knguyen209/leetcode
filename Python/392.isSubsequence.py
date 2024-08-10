'''
https://leetcode.com/problems/is-subsequence
'''

# Approach #1: 

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        arr = []
        for c in s:
            index = t.find(c)
            if index != -1:
                arr.append(index + (0 if len(arr) == 0 else arr[-1]))
                t = t[index+1:len(t)]
        
        if len(arr) != len(s):
            return False

        # Check if the index array is in the ascending order
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        
        return True

# Approach #2: Two Pointers

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Pointer of substring
        i = 0

        # Pointer of string
        j = 0

        if len(s) == 0:
            return True

        while j < len(t) and i < len(s):
            if t[j] == s[i]:
                i += 1
            j += 1
        
        return i == len(s)

s = "abc"
t = "ahbgdc"
print(Solution().isSubsequence(s, t))

s = "axc"
t = "ahbgdc"
print(Solution().isSubsequence(s, t))

s = "twn"
t = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxtxxxxxxxxxxxxxxxxxxxxwxxxxxxxxxxxxxxxxxxxxxxxxxn"
print(Solution().isSubsequence(s, t))

s = "aaaaaa"
t = "bbaaaa"
print(Solution().isSubsequence(s, t))

s = "b"
t = "abc"
print(Solution().isSubsequence(s, t))