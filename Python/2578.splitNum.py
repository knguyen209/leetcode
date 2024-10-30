class Solution:
    def splitNum(self, num: int) -> int:
        nums = [num for num in str(num)]
        nums.sort()
        left = ""
        right = ""

        for i in range(len(nums)):
            if i % 2 == 0:
                left += nums[i]
            else:
                right += nums[i]
        
        return int(left) + int(right)
    
print(Solution().splitNum(4325)) # 59 = 24 + 35
print(Solution().splitNum(687)) # 75 = 68 + 7