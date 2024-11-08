"""
https://leetcode.com/problems/string-compression-iii

Difficulty: Medium
"""

class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""

        counter = 1
        curr = word[0]
        for i in range(1, len(word)):
            if word[i] == curr:
                counter += 1
            else:
                while counter > 0:
                    if counter > 9:
                        comp += "9" + curr
                        counter -= 9
                    else:
                        comp += str(counter) + curr
                        counter = 0

                curr = word[i]
                counter = 1

        while counter > 0:
            if counter > 9:
                comp += "9" + curr
                counter -= 9
            else:
                comp += str(counter) + curr
                counter = 0

        return comp
    

print(Solution().compressedString("aaaaaaaaaaaaaabb")) # Output: 9a5a2b