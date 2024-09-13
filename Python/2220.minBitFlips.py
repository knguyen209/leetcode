"""
https://leetcode.com/problems/minimum-bit-flips-to-convert-number
Difficutly: Easy
"""
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s = bin(start ^ goal)
        count = 0
        for i in range(len(s)):
            if s[i] == "1":
                count += 1
        return count
    
print(Solution().minBitFlips(10, 7))
print(Solution().minBitFlips(3, 4))
