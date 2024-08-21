"""
https://leetcode.com/problems/reverse-vowels-of-a-string/

Difficulty: Easy
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = [c for c in s]
        vowels = ['a','e','i','o','u']
        i = 0
        j = len(arr) - 1

        while i < j:
            if arr[i].lower() not in vowels:
                i += 1
            if arr[j].lower() not in vowels:
                j -= 1
            if arr[i].lower() in vowels and arr[j].lower() in vowels:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        
        return ''.join(arr)
    
print(Solution().reverseVowels("hello")) # Expected: "holle"
print(Solution().reverseVowels("leetcode")) # Expected: "leotcede"