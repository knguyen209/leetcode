"""
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length

Difficulty: Medium
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1

        answer = count

        for i in range(1, len(s) - k + 1):
            if s[i - 1] in vowels:
                count -= 1
            if s[i + k - 1] in vowels:
                count += 1

            answer = max(answer, count)

        return answer
    
s = "abciiidef"
k = 3
print(Solution().maxVowels(s, k))

s = "aeiou"
k = 2
# print(Solution().maxVowels(s, k))

s = "leetcode"
k = 3
# print(Solution().maxVowels(s, k))

print(Solution().maxVowels("weallloveyou", 7))