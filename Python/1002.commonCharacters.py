from typing import List

"""
https://leetcode.com/problems/find-common-characters
Difficulty: Easy
"""
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        answer = []
        arr = [list(w) for w in words]
        words.sort(key=lambda x: len(x))
        max_len_word = words.pop()

        for c in max_len_word:
            flag = True
            
            for a in arr:
                if c not in a:
                    flag = False
                    break
                else:
                    a.remove(c)
                    
            if flag:
                answer.append(c)

        return answer
    
print(Solution().commonChars(["bella","label","roller"])) # ["e","l","l"]
print(Solution().commonChars(["cool","lock","cook"])) # ["c","o"]
