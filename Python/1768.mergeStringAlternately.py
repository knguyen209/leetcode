"""
https://leetcode.com/problems/merge-strings-alternately
Difficulty: Easy
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""

        i = 0
        
        while i < min(len(word1), len(word2)):
            answer += word1[i]
            answer += word2[i]
            i += 1
        
        while i < len(word1):
            answer += word1[i]
            i += 1
        
        while i < len(word2):
            answer += word2[i]
            i += 1

        return answer
    
word1 = "abc"
word2 = "pqr"
print(Solution().mergeAlternately(word1, word2)) # "apbqcr"

word1 = "ab"
word2 = "pqrs"
print(Solution().mergeAlternately(word1, word2)) # "apbqrs"

word1 = "abcd"
word2 = "pq"
print(Solution().mergeAlternately(word1, word2)) # "apbqcd"