"""
https://leetcode.com/problems/power-of-two/

Difficulty: Easy

"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        
        if n % 2 != 0:
            return False
        
        num = 2

        while num <= n:
            if num == n:
                return True
            num = num << 1

        return False

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1 or n == 2:
            return True
        
        if n == 0 or n % 2 != 0:
            return False
        
        str = "{0:b}".format(int(n))

        for i in range(1,len(str)):
            if str[i] == "1":
                return False
            
        return True

    
print(Solution().isPowerOfTwo(16))
print(Solution().isPowerOfTwo(20))
print(Solution().isPowerOfTwo(21))