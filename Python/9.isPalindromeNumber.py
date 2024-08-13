"""
https://leetcode.com/problems/palindrome-numbe
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x == 0:
            return True
        
        if x % 10 == 0:
            return False
        
        arr = []

        while x > 0:
            arr.append(x % 10)
            x = x // 10
        
        i = 0
        j = len(arr) - 1

        while i < j:
            if arr[i] != arr[j]:
                return False
            i += 1
            j -= 1

        return True
    
print(Solution().isPalindrome(121)) # True
# print(Solution().isPalindrome(-121)) # False
# print(Solution().isPalindrome(10)) # False