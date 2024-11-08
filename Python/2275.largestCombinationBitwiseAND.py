from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # The max of bitCounts is the answer
        bitCounts = [0 for _ in range(24)]

        for num in candidates:
            binNum = "{0:b}".format(num)
            n = len(binNum)
            for i in range(n):
                if binNum[i] == "1":
                    bitCounts[n - i - 1] += 1

        return max(bitCounts)
    
print(Solution().largestCombination([16,17,71,62,12,24,14])) # 4
