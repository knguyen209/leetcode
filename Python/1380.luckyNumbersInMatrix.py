from typing import List

"""
https://leetcode.com/problems/lucky-numbers-in-a-matrix/

Difficulty: Easy

A lucky number is an element of the matrix such that 
it is the minimum element in its row and maximum in its column.
"""


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        mins = []
        maxs = []
        for row in matrix:
            mins.append(min(row))

        for n in range(len(matrix[0])):
            cols = []
            for m in range(len(matrix)):
                cols.append(matrix[m][n])
            maxs.append(max(cols))

        intersects = set(mins).intersection(set(maxs))

        return list(intersects)
    
matrix = [[3,7,8],[9,11,13],[15,16,17]]
print(Solution().luckyNumbers(matrix))
# Expected: 15

matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
print(Solution().luckyNumbers(matrix))
# Expected: 12

matrix = [[7,8],[1,2]]
print(Solution().luckyNumbers(matrix))
# Expected: 7