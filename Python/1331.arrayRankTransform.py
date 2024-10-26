from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        my_arr = list(set(arr))
        my_arr.sort()
        rank = 1
        dict = {}
        for num in my_arr:
            dict[num] = rank
            rank += 1
        
        answer = []

        for num in arr:
            answer.append(dict[num])

        return answer
    
print(Solution().arrayRankTransform([40,10,20,30])) # [4,1,2,3]
print(Solution().arrayRankTransform([100, 100, 100])) # [1,1,1]
print(Solution().arrayRankTransform([37,12,28,9,100,56,80,5,12])) # [5,3,4,2,8,6,7,1,3]