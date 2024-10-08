"""
https://leetcode.com/problems/fibonacci-number/

Difficulty: Easy

"""
class Solution:
    def fib(self, n: int) -> int:
        f = [0, 1]
        for i in range (2, n + 1):
            f.append(f[i - 1] + f[i - 2])

        return f[n]
    
print(Solution().fib(2))
print(Solution().fib(3))
print(Solution().fib(4))
print(Solution().fib(5))