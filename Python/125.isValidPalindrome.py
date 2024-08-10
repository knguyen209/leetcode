'''
https://leetcode.com/problems/valid-palindrome
'''

# Approach 1: Two Pointer
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = s.lower()
        start = 0
        end = len(str) - 1
        
        while start < end:
            
            if not (str[start].isalpha() or str[start].isdigit()):
                start += 1
                continue

            if not (str[end].isalpha() or str[end].isdigit()):
                end -= 1
                continue    

            if str[start] != str[end]:
                return False
            else:
                start += 1
                end -= 1

        return True
    
# Approach 2:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = ''
        for c in s.lower():
            if c.isalpha() or c.isdigit():
                str += c
        
        n = len(str)
        mid = n // 2
        
        first_half_str = str[0:mid]
        second_half_str = str[mid:n] if n % 2 == 0 else str[mid+1:n]
        second_half_str = list(second_half_str)
        second_half_str.reverse()
        second_half_str = ''.join(second_half_str)
        
        
        return first_half_str == second_half_str
    
s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))

s = "race a car"
print(Solution().isPalindrome(s))

s = "abba"
print(Solution().isPalindrome(s))

s = "abcba"
print(Solution().isPalindrome(s))