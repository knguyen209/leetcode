from typing import List

"""
https://leetcode.com/problems/string-matching-in-an-array/
Difficulty: Easy
"""

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        answer = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    answer.append(words[i])

        return set(answer)
    
str1 = "hello"
str2 = "ll"

print(str2 in str1)

words = ["mass","as","hero","superhero"]
print(Solution().stringMatching(words))