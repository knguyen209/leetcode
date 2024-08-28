"""
https://leetcode.com/problems/min-stack

Difficulty: Medium

"""
    
# O(1) Solution:
    
class MinStack:

    def __init__(self):
        # A stack of tuple, each tuple stores the value and the min val at that position
        # Ex: [(-2, -2), (-1, -2)]
        self._stack = []
        
    def push(self, val: int) -> None:
        if len(self._stack) == 0:
            self._stack.append((val, val))
            return
        
        if val < self._stack[-1][1]:
            self._stack.append((val, val))
        else:
            self._stack.append((val, self._stack[-1][1]))
        
    # removes the element on the top of the stack. (i.e. last element in the array)
    def pop(self) -> None:
        self._stack = self._stack[:-1]

    def top(self) -> int:
        return self._stack[-1][0]
        
    def getMin(self) -> int:
        return self._stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# ["MinStack","push","push","push","getMin","top","pop","getMin"]
# [[],[-2],[0],[-1],[],[],[],[]]

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-1)
print(obj.getMin())
print(obj.top())
print(obj.pop())
print(obj.getMin())

# ["MinStack","push","push","push","getMin","pop","getMin"]
# [[],[0],[1],[0],[],[],[]]

