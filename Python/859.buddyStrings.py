"""
https://leetcode.com/problems/buddy-strings/
Difficulty: Easy
"""
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)

        if len(goal) != n:
            return False;

        if s == goal:
            temp = set(s)
            return len(temp) < len(goal)  # Swapping same characters

        i = 0
        j = n - 1

        while i < j and s[i] == goal[i]:
            i += 1

        while j >= 0 and s[j] == goal[j]:
            j -= 1

        if i < j:
            s_list = list(s)
            s_list[i], s_list[j] = s_list[j], s_list[i]
            s = ''.join(s_list)

        return s == goal

    
print(Solution().buddyStrings("ab","ba")) # True
print(Solution().buddyStrings("ab","ab")) # False
print(Solution().buddyStrings("aa","aa")) # True