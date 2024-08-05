from typing import List

"""
https://leetcode.com/problems/kth-distinct-string-in-an-array
"""
class Solution:
    
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}

        # Count the frequency of each str
        for str in arr:
            if str in count:
                count[str] += 1
            else:
                count[str] = 1
        
        # Filter for string that appears only once
        distinct_strs = [str for str in arr if count[str] == 1]
        
        # Return the k-th distinct string
        return "" if k > len(distinct_strs) else distinct_strs[k - 1]

arr = ["d","b","c","b","c","a"]
k = 2

result = Solution().kthDistinct(arr, 2)
print(result)