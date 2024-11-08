class Solution:
    def minChanges(self, s: str) -> int:
        answer = 0
        
        i = 0
        while i < len(s) - 1:
            if s[i] != s[i + 1]:
                answer += 1
            i += 2

        return answer
        

print(Solution().minChanges("1001"))
print(Solution().minChanges("10"))
print(Solution().minChanges("000000"))