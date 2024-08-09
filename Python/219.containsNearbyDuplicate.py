# # https://leetcode.com/problems/contains-duplicate-ii/

from typing import List


# Approach #1: Sliding Window

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(0, len(nums)):
            sub_arr = nums[i+1:i+k+1]
            if nums[i] in sub_arr:
                return True
        return False
    
# Approach #2: Hash Map
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}
        for i in range(0, len(nums)):
            if nums[i] not in map:
                # Add the index of the number to the map
                map[nums[i]] = i
            else:
                # Get the previous index of the number
                # Check if the distance is less than or equal to k
                if abs(map[nums[i]] - i) <= k:
                   return True
                else:
                    # If distance is greater than k, update new index
                    map[nums[i]] = i
        return False


nums = [1,2,3,1]
k = 3
print(Solution().containsNearbyDuplicate(nums, k))

nums = [1,0,1,1]
k = 1
print(Solution().containsNearbyDuplicate(nums, k))

nums = [1,2,3,1,2,3]
k = 2
print(Solution().containsNearbyDuplicate(nums, k))