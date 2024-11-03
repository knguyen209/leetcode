class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        
        if len(words) == 1:
            return sentence[0] == sentence[-1]
        
        if words[0][0] != words[-1][-1]:
            return False
        
        for x, y in zip(words, words[1:]):
            if x[-1] != y[0]:
                return False

        return True

print(Solution().isCircularSentence("leetcode exercises sound delightful")) # True
print(Solution().isCircularSentence("eetcode")) # True
print(Solution().isCircularSentence("Leetcode is cool")) # False