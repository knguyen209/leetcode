"""
https://leetcode.com/problems/pascals-triangle
Difficulty: Easy
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answers = []

        if numRows >= 1:
            answers.append([1])
        
        if numRows >= 2:
            answers.append([1,1])
        
        curr = 3
        
        while curr <= numRows:
            arr = [1]
            prev_row = answers[-1]
            
            for i in range(curr - 2):
                arr.append(prev_row[i] + prev_row[i + 1])
            
            arr.append(1)
            answers.append(arr)
            curr += 1
            

        return answers
    
print(Solution().generate(5))