"""
https://leetcode.com/problems/reverse-words-in-a-string
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        arr = [w for w in arr if len(w) > 0]
        str = ""
        while len(arr) > 0:
            str += arr.pop() + " "
        
        return str.strip()

# Two Pointers Approach:

class Solution:
    def reverseWords(self, s: str) -> str:
        arr = []
        i = 0
        startIndex = 0
        endIndex = 0
        while i < len(s):
            if s[i] != ' ':
                endIndex = i
            else:
                str = s[startIndex:endIndex+1]
                if str != ' ':
                    arr.insert(0, str)
                str = ''
                startIndex = i + 1
                endIndex = i + 1
            i += 1
        
        str = s[startIndex:endIndex+1]
        
        if len(str) > 0:
            arr.insert(0, str)

        # arr = [w for w in arr if w not in [' ', '']]
        
        return ' '.join(arr)
    
print(Solution().reverseWords("the sky is blue"))
print(Solution().reverseWords("  hello world  "))
print(Solution().reverseWords(" asdasd df f"))