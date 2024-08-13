"""
https://leetcode.com/problems/sqrtx
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        low, high = 1, x
        
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return high
    
print(Solution().mySqrt(4))
print(Solution().mySqrt(8))
print(Solution().mySqrt(25))



# def mySQqrt(n):
#     if n < 2:
#         return n
#     low, high = 1, n
#     while low <= high:
#         mid = (low + high) // 2
#         if mid * mid == n:
#             return mid
#         elif mid * mid < n:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return high
 
 
# n=25
# print(mySQqrt(n))