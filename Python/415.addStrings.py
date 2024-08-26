"""
https://leetcode.com/problems/add-strings/

Difficulty: Easy

"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        i = -1
        answer = ""
        remainder = 0

        while i >= -(len(num2)):
            n1 = int(num1[i])
            n2 = int(num2[i])
            answer = str((n1 + n2 + remainder) % 10) + answer
            remainder = (n1 + n2 + remainder) // 10
            i -= 1
        
        while i >= -(len(num1)):
            n1 = int(num1[i])
            answer = str((n1 + remainder) % 10) + answer
            remainder = (n1 + remainder) // 10
            i -= 1

        if remainder > 0:
            answer = str(remainder) + answer

        return answer
    
print(Solution().addStrings("11", "123")) # 134
print(Solution().addStrings("456", "77")) # 533
print(Solution().addStrings("0", "2")) # 2
print(Solution().addStrings("1", "9")) # 10
