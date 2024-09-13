"""
https://leetcode.com/problems/count-the-number-of-special-characters-i/

Difficulty: Easy
"""

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        answer = 0
        uppercases = set()
        lowercases = set()

        for i in range(len(word)):
            if str.islower(word[i]):
                lowercases.add(word[i])
            else:
                uppercases.add(word[i])
        
        for i in lowercases:
            if i.upper() in uppercases:
                answer += 1
        
        return answer
    
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        answer = 0

        for i in range(len(alphabets)):
            if alphabets[i] in word and alphabets[i].upper() in word:
                answer += 1

        return answer
    
print(Solution().numberOfSpecialChars("aaAbcBC"))   # 3
print(Solution().numberOfSpecialChars("abc"))       # 0
print(Solution().numberOfSpecialChars("abBCab"))    # 1
print(Solution().numberOfSpecialChars("AA"))        # 0
print(Solution().numberOfSpecialChars("Cc"))        # 1