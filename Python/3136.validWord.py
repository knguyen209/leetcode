class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
    
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowelCount = 0
        consonantCount = 0

        for c in word:
            if str.isalnum(c):
                if str.isalpha(c):
                    if c.lower() in vowels:
                        vowelCount += 1
                    else:
                        consonantCount += 1
            else:
                return False
        
        if vowelCount < 1 or consonantCount < 1:
            return False
        
        return True
    
print(Solution().isValid("234Adas"))    # True
print(Solution().isValid("b3"))         # False
print(Solution().isValid("a3$e"))       # False
