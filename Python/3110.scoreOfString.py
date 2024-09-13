"""
https://leetcode.com/problems/score-of-a-string/

Difficulty: Easy
"""

class Solution:
    def scoreOfString(self, s: str) -> int:
        answer = 0
        
        for i in range(1, len(s)):
            answer += abs(ord(s[i]) - ord(s[i - 1]))

        return answer
    
print(Solution().scoreOfString("hello"))
print(Solution().scoreOfString("zaz"))