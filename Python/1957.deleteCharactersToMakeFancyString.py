class Solution:
    def makeFancyString(self, s: str) -> str:
        s += "  "
        answer = ""
        
        for a, b, c in zip(s[:], s[1:], s[2:]):
            if a == b == c:
                continue

            answer += a

        return answer

print(Solution().makeFancyString("leeetcode"))