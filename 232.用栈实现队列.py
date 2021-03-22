#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.prestack = []
        self.poststack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while len(self.poststack) != 0:
            self.prestack.append(self.poststack.pop())
        self.prestack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.prestack:
            self.poststack.append(self.prestack.pop())
        if self.poststack:
            return self.poststack.pop()
        else:
            return -1
    def peek(self) -> int:
        """
        Get the front element.
        """
        while self.prestack:
            self.poststack.append(self.prestack.pop())
        if self.poststack:
            return self.poststack[-1]
        else:
            return -1        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.prestack and not self.poststack:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

