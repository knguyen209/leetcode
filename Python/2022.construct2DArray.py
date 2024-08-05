from typing import List

# """
# https://leetcode.com/problems/convert-1d-array-into-2d-array/
# """

"""
Approach #1
"""

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        """
        original: original array
        m: number of rows
        n: number of columns
        """

        # Return an empty array if not fits
        if len(original) != m * n:
            return []
        
        arr = []
        row = []
        for item in original:
            # Initialize a new row if the row array is full
            if len(row) == n:
                arr.append(row)
                row = []
                
            row.append(item)

        # Add the last row to the result array
        arr.append(row)

        return arr


"""
Approach #2: Slicing array
"""
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        """
        original: original array
        m: number of rows
        n: number of columns
        """

        # Return an empty array if not fits
        if len(original) != m * n:
            return []
        
        arr = []
        
        for i in range(0, m):
            start = i * n
            end = (i + 1) * n
            arr.append(original[start:end])

        return arr

        

original = [1,2,3,4] 
m = 2
n = 2

result = Solution().construct2DArray(original, m, n)
print(result)

original = [1,2,3] 
m = 1
n = 3

result = Solution().construct2DArray(original, m, n)
print(result)

original = [1,2] 
m = 1
n = 1

result = Solution().construct2DArray(original, m, n)
print(result)