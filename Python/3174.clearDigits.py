"""
https://leetcode.com/problems/clear-digits/
Difficulty: Easy
"""
class Solution:
    def clearDigits(self, s: str) -> str:
        answer = ""
        i = len(s) - 1
        digit_count = 0
        while i >= 0:
            if str.isdigit(s[i]):
                digit_count += 1
            else:
                if digit_count > 0:
                    digit_count -= 1
                else:
                    answer = s[i] + answer
            i -= 1

        return answer
    
print(Solution().clearDigits("abc"))
print(Solution().clearDigits("cb34"))