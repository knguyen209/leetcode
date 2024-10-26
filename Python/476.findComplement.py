"""
https://leetcode.com/problems/number-complement/

Difficulty: Easy
"""
class Solution:
    def findComplement(self, num: int) -> int:
        bin_val = bin(num)[2:]
        str = ""
        
        for i in bin_val:
            str += "0" if i == "1" else "1"
        
        return int(str, 2)
    
print(Solution().findComplement(5)) # 2
print(Solution().findComplement(1)) # 0
