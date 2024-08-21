from typing import List

"""
https://leetcode.com/problems/reverse-string/
Difficulty: Easy
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        print(s)

        

Solution().reverseString(["h","e","l","l","o"])
Solution().reverseString(["H","a","n","n","a","h"])
        