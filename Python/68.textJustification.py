from typing import List

"""
https://leetcode.com/problems/text-justification

Difficult: Hard

"""

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        answer = []
        arr = []
        curr = ''

        for i in range(len(words)):
            curr = ' '.join(arr)
            
            if len(curr) + len(words[i]) < maxWidth:
                arr.append(words[i])
            else:
                str = self.joinWords(arr, maxWidth)
                if len(str) > 0:
                    answer.append(str)
                arr = [words[i]]
             
        
        if len(arr) > 0:
            last_line = ' '.join(arr)
            
            if len(last_line) <= maxWidth:
                last_line += ' ' * (maxWidth - len(last_line))
                answer.append(last_line)
            else:
                answer.append(self.joinWords(arr[0:len(arr)-1], maxWidth))
                answer.append(words[-1] + ' ' * (maxWidth - len(words[-1])))

        return [sentence for sentence in answer if len(sentence) > 0]
    
    def joinWords(self, words: List[str], maxWidth: int) -> str:
        if len(words) > 1:
            avaible_space = maxWidth - len(''.join(words))
            
            arr = [1 for _ in range(len(words) - 1)]
            
            avaible_space = avaible_space - len(arr)
            while avaible_space > 0:
                for i in range(len(arr)):
                    avaible_space -= 1
                    arr[i] += 1
                    if avaible_space == 0:
                        break
            
            str = ''
            for i in range(len(arr)):
                str += words[i] + (' ' * arr[i])
            str += words[-1]
            
            return str
        elif len(words) == 1:
            return words[0] + (' ' * (maxWidth - len(words[0])))
        else:
            return ''

words = ["What","must","be","shall","be."]
maxWidth = 5
print(Solution().fullJustify(words, maxWidth))

words = ["a"]
maxWidth = 1
print(Solution().fullJustify(words, maxWidth))

words = ["Listen","to","many,","speak","to","a","few."]
maxWidth = 6
print(Solution().fullJustify(words, maxWidth))

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(Solution().fullJustify(words, maxWidth))

words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
print(Solution().fullJustify(words, maxWidth))

words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
print(Solution().fullJustify(words, maxWidth))

# words = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
# maxWidth = 16
# print(Solution().fullJustify(words, maxWidth))

