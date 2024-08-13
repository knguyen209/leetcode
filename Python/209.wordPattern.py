'''
https://leetcode.com/problems/word-pattern
'''


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict = {}
        sDict = {}
        arr = s.split(' ')
        
        # Edge cases:
        if len(arr) == 1:
            return len(pattern) == 1
        
        strArr = []

        for i in range(0, len(pattern)):
            if not dict.get(pattern[i]) and not sDict.get(arr[i]):
                dict[pattern[i]] = arr[i]
                sDict[arr[i]] = pattern[i]
                strArr.append(dict[pattern[i]])
            elif not dict.get(pattern[i]) or not sDict.get(arr[i]):
                return False
            else:
                if dict[pattern[i]] == arr[i] and sDict[arr[i]] == pattern[i]:
                    strArr.append(dict[pattern[i]])
                else:
                    return False

        str = ' '.join(strArr)
        return str == s


pattern = "abba"
s = "dog cat cat dog"
print(Solution().wordPattern(pattern, s)) # True

pattern = "e"
s = "eukera"
print(Solution().wordPattern(pattern, s)) # True

pattern = "abba"
s = "dog cat cat fish"
print(Solution().wordPattern(pattern, s)) # False

pattern = "abba"
s = "dog dog dog dog"
print(Solution().wordPattern(pattern, s)) # False

pattern = "jquery"
s = "jquery"
print(Solution().wordPattern(pattern, s)) # False