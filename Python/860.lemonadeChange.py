"""
https://leetcode.com/problems/lemonade-change/

Difficulty: Easy
"""
from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_changes = 0
        ten_changes = 0
        twenty_changes = 0

        for bill in bills:
            if bill == 5:
                five_changes += 1
            if bill == 10:
                if five_changes > 0:
                    five_changes -= 1
                    ten_changes += 1
                else:
                    return False
            if bill == 20:
                if five_changes > 0 and ten_changes > 0:
                    five_changes -= 1
                    ten_changes -= 1
                    twenty_changes += 1
                elif five_changes >= 3:
                    five_changes -= 3
                    twenty_changes += 1
                else:
                    return False

        return True
    
bills = [5,5,5,10,20]
print(Solution().lemonadeChange(bills))

bills = [5,5,10,10,20]
print(Solution().lemonadeChange(bills))