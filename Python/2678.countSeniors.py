"""
https://leetcode.com/problems/number-of-senior-citizens

Difficulty: Easy
"""

from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        answer = 0
        for detail in details:
            age = int(detail[11:13])
            if age > 60:
                answer += 1
                
        return answer
    
details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
print(Solution().countSeniors(details))