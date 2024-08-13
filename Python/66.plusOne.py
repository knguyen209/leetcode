"""
https://leetcode.com/problems/plus-one
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        base = 0

        while len(digits) > 0:
            num += digits[-1] * (10 ** base)
            base += 1
            digits.pop()
        
        num += 1
        
        arr = []
        
        while num > 0:
            arr.append(num % 10)
            num = num // 10
        
        arr.reverse()
        
        return arr
    
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        
        carried = 0

        while i >= 0:
            if i == len(digits) - 1:
                carried = 1

            curr = digits[i]
            
            if curr + carried >= 10:
                digits[i] = (curr + carried) % 10
                carried = (curr + carried) // 10
            else:
                digits[i] = digits[i] + carried
                carried = 0

            i -= 1

        if carried > 0:
            digits.insert(0, carried)

        return digits

digits = [1,2,3]
print(Solution().plusOne(digits))
# Expect: [1,2,4]

digits = [4,3,2,1]
print(Solution().plusOne(digits))
# Expect: [4,3,2,2]

digits = [9]
print(Solution().plusOne(digits))
# Expect: [1,0]

# arr = [1,2,3,4]
# arr.insert(0, 5)
# print(arr)
