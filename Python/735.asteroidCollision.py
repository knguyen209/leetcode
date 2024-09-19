from typing import List

"""
https://leetcode.com/problems/asteroid-collision

Difficulty: Easy
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = len(asteroids) - 1
        answer = []
        while i > 0:
            if (asteroids[i] < 0 and asteroids[i - 1] > 0) or (asteroids[i] > 0 and asteroids[i - 1] < 0):
                if abs(asteroids[i - 1]) < abs(asteroids[i]):
                    asteroids[i - 1] = asteroids[i]
                    asteroids.pop()
                elif abs(asteroids[i - 1]) > abs(asteroids[i]):
                    asteroids.pop()
                else:
                    asteroids.pop()
                    asteroids.pop()
                    i -= 1
            i -= 1
        return answer
    
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for a in asteroids:
            while st and a < 0 < st[-1]:
                if -a > st[-1]:
                    st.pop()
                    continue
                elif -a == st[-1]:
                    st.pop()
                break
            else:
                st.append(a)
                    
        return st

    

print(Solution().asteroidCollision([5,10,-5])) # [5,10]
# print(Solution().asteroidCollision([8,-8])) # []
# print(Solution().asteroidCollision([10,2,-5])) # [10]
# print(Solution().asteroidCollision([-2,-1,1,2])) # [-2,-1,1,2]
