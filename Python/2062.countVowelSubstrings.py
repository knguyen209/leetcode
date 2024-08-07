"""
https://leetcode.com/problems/count-vowel-substrings-of-a-string/
"""

"""
A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') 
and has all five vowels present in it.
"""

"""
Approach #1: Sliding Window
"""
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        if len(word) < 5:
            return 0

        vowels = set(['a', 'e', 'i', 'o', 'u'])
        count = 0
        window_size = len(word)
        while window_size >= 5:
            for i in range(0, len(word) - window_size + 1):
                substr = word[i:i+window_size]
                if set(substr) == vowels:
                    count += 1
            window_size -= 1

        return count
    
"""
Approach #2: O(n)
"""
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        if len(word) < 5:
            return 0

        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        last_consonant_index = -1
        last_seen_vowels = {v: -2 for v in vowels}

        for i, c in enumerate(word):
            if c not in vowels:
                last_consonant_index = i
            else:
                last_seen_vowels[c] = i
                count += max(min(last_seen_vowels.values()) - last_consonant_index, 0)

        return count


word = "aeiouu"
result = Solution().countVowelSubstrings(word)
print(result) # Expect: 2 "aeiou", "aeiouu"

word = "unicornarihan"
result = Solution().countVowelSubstrings(word)
print(result) # Expect: 0 

word = "cuaieuouac"
result = Solution().countVowelSubstrings(word)
print(result) # Expect: 7

word = "poazaeuioauoiioaouuouaui"
result = Solution().countVowelSubstrings(word)
print(result) # Expect: 7
