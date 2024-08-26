"""
https://leetcode.com/problems/longest-palindrome/description/

Difficulty: Easy
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        map = Counter(s)
        length = 0
        exist_odd = False
        for c in map:
            if map[c] % 2 == 0:
                length += map[c]
            else:
                length += (map[c] - 1)
                exist_odd = True
                
        return (length + 1) if exist_odd else length
    
print(Solution().longestPalindrome("abccccdd")) # 7
print(Solution().longestPalindrome("a")) # 1
print(Solution().longestPalindrome("bb")) # 2
print(Solution().longestPalindrome("aaaAaaaa")) # 2
print(Solution().longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth")) # 983