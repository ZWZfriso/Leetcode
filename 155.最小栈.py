#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self,):
        self.istack = []
        self.minstack = []

    def push(self, x: int) -> None:
        self.istack.append(x)
        if len(self.minstack) != 0 and self.minstack[-1] < x:
            temp = self.minstack[-1]
            self.minstack.append(temp)
        else:
            self.minstack.append(x)

    def pop(self) -> None:
        if len(self.istack) == 0:
            return
        self.istack = self.istack[:-1]
        self.minstack = self.minstack[:-1]

    def top(self) -> int:
        if len(self.istack) == 0:
            return 0
        return self.istack[-1]

    def getMin(self) -> int:
        if len(self.istack) == 0:
            return float('inf')
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

