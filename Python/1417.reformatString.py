"""
https://leetcode.com/problems/reformat-the-string/description/

Difficulty: Easy
"""

class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        digits = []

        for i in range(len(s)):
            if s[i] >= "0" and s[i] <= "9":
                digits.append(s[i])
            else:
                letters.append(s[i])

        answer = ""

        if abs(len(letters) - len(digits)) > 1:
            return ""
        
        if len(letters) > len(digits):
            for i in range(len(digits)):
                answer += letters[i] + "" + digits[i]

            answer += letters[-1]
        elif len(letters) < len(digits):
            for i in range(len(letters)):
                answer += digits[i] + "" + letters[i]

            answer += digits[-1]
        else:
            for i in range(len(letters)):
                answer += digits[i] + "" + letters[i]
            return answer

        return answer
    
print(Solution().reformat("a0b1c2")) # "0a1b2c"
print(Solution().reformat("leetcode")) # ""
print(Solution().reformat("1229857369")) # ""
print(Solution().reformat("ab123")) # "1a2b3"
