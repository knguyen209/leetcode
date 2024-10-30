from typing import List

"""
https://leetcode.com/problems/keyboard-row

Difficulty: Easy
"""

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set(list("qwertyuiop"))
        second_row = set(list("asdfghjkl"))
        last_row = set(list("zxcvbnm"))

        answers = []
        for word in words:
            set_word = set(list(word.lower()))
            if set_word.issubset(first_row) or set_word.issubset(second_row) or set_word.issubset(last_row):
                answers.append(word)

        return answers
    
print(Solution().findWords(["Hello","Alaska","Dad","Peace"])) 
print(Solution().findWords(["omk"]))
print(Solution().findWords(["adsdf","sfd"])) 