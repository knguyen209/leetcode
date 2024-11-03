"""
https://leetcode.com/problems/rotate-string/
Difficulty: Easy

Insight: Concatenate a string with itself (s + s) 
will contain all possible rotations of the original string.
"""
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in s + s
    
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
            
        if s == goal:
            return True
        
        arr = [c for c in goal]
        
        for _ in range(len(s)):
            if "".join(arr) == s:
                return True
            else:
                first = arr.pop(0)
                arr.append(first)
        
        return False
        
s = "abcde"
goal = "cdeab"

print(Solution().rotateString(s, goal)) # True

s = "abcde"
goal = "abced"
print(Solution().rotateString(s, goal)) # False