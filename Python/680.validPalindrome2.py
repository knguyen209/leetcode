"""
https://leetcode.com/problems/valid-palindrome-ii/

Difficulty: Easy
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        attempts = 0

        def validPalindromeRange(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        while left <= right:
            if s[left] != s[right]:
                return validPalindromeRange(left + 1, right) or validPalindromeRange(left, right - 1)
        
            left += 1
            right -= 1
        return True
    
print(Solution().validPalindrome("aba")) # True
print(Solution().validPalindrome("abca")) # True
print(Solution().validPalindrome("abc")) # False
print(Solution().validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")) # False
"""
cupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuc_u
"""
