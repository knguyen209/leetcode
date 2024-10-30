"""
https://leetcode.com/problems/maximum-number-of-moves-in-a-grid

Difficulty: Medium
"""
from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid) # num of rows
        n = len(grid[0]) # num of cols

        maxOp = 0

        dp = [0] * m

        direction = [-1, 0, 1]

        for j in range(1, n):
            dp2 = dp[:]

            for i in range(m):
                for x in direction:
                    new_i = i + x
                    new_j = j - 1

                    if 0 <= new_i < m and 0 <= new_j < n and grid[i][j] > grid[new_i][new_j] and dp[new_i] == new_j:
                        dp2[i] = j
                        maxOp = max(maxOp, j)
                        break

            dp = dp2[:]
        
        return maxOp
        
    
    
grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
print(Solution().maxMoves(grid)) # 3

grid = [[3,2,4],[2,1,9],[1,1,7]]
print(Solution().maxMoves(grid)) # 0

grid = [[1000000,92910,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068],[1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1091,1092,1093,1094,1095,1096,1097,1098,1099,1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118]]
print(Solution().maxMoves(grid)) # 49

grid = [[187,167,209,251,152,236,263,128,135],[267,249,251,285,73,204,70,207,74],[189,159,235,66,84,89,153,111,189],[120,81,210,7,2,231,92,128,218],[193,131,244,293,284,175,226,205,245]]
print(Solution().maxMoves(grid)) # 3
