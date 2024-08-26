from typing import List

"""
https://leetcode.com/problems/fizz-buzz/

Difficulty: Easy
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        for i in range(1, n + 1):
            s = ""
            if i % 3 == 0:
                s += "Fizz"
            if i % 5 == 0:
                s += "Buzz"
            if len(s) == 0:
                s += str(i)
            answer.append(s)

        return answer
    
print(Solution().fizzBuzz(15)) 