#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        istack = []
        for i in range(0, len(s)):
            if s[i] == ']':
                # 找字符串
                temp = []
                while len(istack) > 0 and istack[-1] != '[':
                    temp.insert(0, istack[-1])
                    istack = istack[:-1]
                istack = istack[:-1]
                # 找数字
                number = 1
                ilen = len(istack)
                while ilen >= number and istack[ilen - number] in ['0','1','2','3','4','5','6','7','8','9']:
                    number += 1
                # 数字范围：[len - i + 1, len - 1]
                res = int(''.join(istack[ilen - number + 1:]))
                istack = istack[:ilen - number + 1]
                # 复制
                for i in range(0, res):
                    istack.extend(temp)
            else:
                istack.append(s[i])
        return ''.join(istack)
# @lc code=end

