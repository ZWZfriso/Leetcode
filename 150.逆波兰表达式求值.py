#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return 0
        istack = []
        for i in range(0, len(tokens)):
            if tokens[i] not in ["+", "-", "*", "/"]:
                istack.append(int(tokens[i]))
            elif len(istack) < 2:
                break
            else:
                a, b = istack[-2], istack[-1]
                istack = istack[:-2]
                if tokens[i] == "+":
                    istack.append(a + b)
                elif tokens[i] == "-":
                    istack.append(a - b)
                elif tokens[i] == "*":
                    istack.append(a * b)
                elif tokens[i] == "/":
                    istack.append(int(a / b))
                else:
                    pass
        if len(istack) == 1:
            return istack[0]
        else:
            return 0
# @lc code=end

