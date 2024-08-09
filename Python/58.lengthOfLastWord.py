"""
https://leetcode.com/problems/length-of-last-word
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str = s.strip()
        arr = str.split(" ")
        return len(arr[-1])

    
print(Solution().lengthOfLastWord("Hello World"))
print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
print(Solution().lengthOfLastWord("luffy is still joyboy"))