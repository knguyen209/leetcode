from typing import List

"""
https://leetcode.com/problems/counting-bits/?envType=study-plan-v2&envId=leetcode-75
Difficulty: Easy
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [0]
        for i in range(1, n + 1):
            answer.append(answer[i // 2] + i % 2)
        return answer
    
print(Solution().countBits(5)) # [0,1,1,2,1,2]