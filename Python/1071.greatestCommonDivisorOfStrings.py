class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        import math
        
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        if str2 in str1:
            gcd = math.gcd(len(str1), len(str2))
            s1 = str1[:gcd] * (len(str1) // gcd)
            s2 = str2[:gcd] * (len(str2) // gcd)
            if s1 == str1 and s2 == str2 and str1[:gcd] == str2[:gcd]:
                return str1[:gcd]
        
        return ""
    
str1 = "ABCABC"
str2 = "ABC"
print(Solution().gcdOfStrings(str1, str2)) # "ABC"

str1 = "ABABAB"
str2 = "ABAB"
print(Solution().gcdOfStrings(str1, str2)) # "AB"

str1 = "LEET"
str2 = "CODE"
print(Solution().gcdOfStrings(str1, str2)) # ""

str1 = "ABCDEF"
str2 = "ABC"
print(Solution().gcdOfStrings(str1, str2)) # ""

str1 = "BABABA"
str2 = "ABAB"
print(Solution().gcdOfStrings(str1, str2)) # ""