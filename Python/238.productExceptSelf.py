"""
https://leetcode.com/problems/product-of-array-except-self

Difficulty: Medium
"""
from typing import List

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         totalProduct = 1
#         answer = []

#         for i in range(len(nums)):
#             totalProduct *= nums[i]

#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 answer.append(totalProduct // nums[i])
#             else:
#                 answer.append(totalProduct)

#         return answer

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        
        prefix_product = 1
        suffix_product = 1

        for i in range(len(nums)):
            if i > 0:
                prefix_product *= nums[i - 1]
                prefix.append(prefix_product)
            else:
                prefix.append(1)

            if i > 0:
                suffix_product *= nums[-i]
                suffix.append(suffix_product)
            else:
                suffix.append(1)
            
        answer = []

        suffix.reverse()

        # print(nums)
        # print(prefix)
        # print(suffix)

        for i in range(len(nums)):
            answer.append(prefix[i] * suffix[i])

        return answer

    
nums = [1,2,3,4]
print("ANSWER", Solution().productExceptSelf(nums)) # [24,12,8,6]

nums = [-1,1,0,-3,3]
print("ANSWER", Solution().productExceptSelf(nums)) # [0,0,9,0,0]

