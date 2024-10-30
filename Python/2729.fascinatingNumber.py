"""
https://leetcode.com/problems/check-if-the-number-is-fascinating/
"""
class Solution:
    def isFascinating(self, n: int) -> bool:
        if n % 5 == 0 or n % 10 == 0:
            return False
        
        num = str(n) + str(n * 2) + str(n * 3)
        print(num)
        arr = [0] * 9
        for c in num:
            if c == "0":
                return False
            arr[int(c) - 1] += 1
            if arr[int(c) - 1] > 1:
                return False
        print(arr)
        return True

print(Solution().isFascinating(192))
print(Solution().isFascinating(267))