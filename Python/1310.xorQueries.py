from typing import List

"""
https://leetcode.com/problems/xor-queries-of-a-subarray/
Difficulty: Medium
"""

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        prefixArr = [arr[0]]
        
        for i in range(1, len(arr)):
            prefixArr.append(prefixArr[i - 1] ^ arr[i])
        
        for query in queries:
            if query[0] == query[1]:
                answer.append(arr[query[0]])
                continue

            if query[0] == 0:
                answer.append(prefixArr[query[1]])

            if query[0] > 0:
                answer.append(prefixArr[query[0] - 1] ^ prefixArr[query[1]])
            
        return answer
    
arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
print(Solution().xorQueries(arr, queries))