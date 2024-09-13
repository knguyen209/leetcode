"""
https://leetcode.com/problems/removing-stars-from-a-string
Difficulty: Medium
"""

class Solution:
    def removeStars(self, s: str) -> str:
        stack = list(s)
        answer = ""
        count = 0
        while len(stack) > 0:
            last = stack.pop()
            if last == "*":
                count += 1
            else:
                if count == 0:
                    answer = last + answer
                else:
                    count -= 1

        return answer
    
print(Solution().removeStars("leet**cod*e")) # "lecoe"
print(Solution().removeStars("erase*****")) # ""
