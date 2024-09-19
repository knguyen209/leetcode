from typing import List

"""
https://leetcode.com/problems/uncommon-words-from-two-sentences

Difficulty: Easy
"""

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        from collections import Counter
        dict1 = Counter(s1.split(' '))
        dict2 = Counter(s2.split(' '))
        arr1 = [word for word in dict1 if dict1[word] == 1]
        arr2 = [word for word in dict2 if dict2[word] == 1]
        answer = []
        
        for word in set(arr1).difference(set(arr2)).union(set(arr2).difference(set(arr1))):
            answer.append(word)
        
        return answer
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        from collections import Counter
        dict1 = Counter(s1.split(' '))
        dict2 = Counter(s2.split(' '))
        answer = []

        for word in dict1:
            if dict1[word] == 1 and word not in dict2:
                answer.append(word)
        
        for word in dict2:
            if dict2[word] == 1 and word not in dict1:
                answer.append(word)

        return answer
    
s1 = "this apple is sweet"
s2 = "this apple is sour"
print(Solution().uncommonFromSentences(s1, s2))
print(Solution().uncommonFromSentences("s z z z s", "s z ejt"))