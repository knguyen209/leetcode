"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1

        if haystack == needle:
            return 0
        
        for i in range(0, len(haystack)):
            end = i + len(needle)
            substr = haystack[i:end]
            if substr == needle:
                return i

        return index

    
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            index = haystack.index(needle)
            return index
        except:
            return -1
        

haystack = "sadbutsad"
needle = "sad"
result = Solution().strStr(haystack, needle)
print(result)

haystack = "leetcode"
needle = "leeto"
result = Solution().strStr(haystack, needle)
print(result)

haystack = "a"
needle = "a"
result = Solution().strStr(haystack, needle)
print(result)

haystack = "abc"
needle = "c"
result = Solution().strStr(haystack, needle)
print(result)