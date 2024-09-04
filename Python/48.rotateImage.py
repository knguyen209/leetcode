from typing import List

"""
https://leetcode.com/problems/rotate-image

Difficulty: Medium

"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        arr = [[False for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if not arr[i][j] and not arr[j][i]:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    arr[i][j] = True
                    arr[j][i] = True

        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]


matrix = [[1,2,3],[4,5,6],[7,8,9]]
Solution().rotate(matrix)

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Solution().rotate(matrix)