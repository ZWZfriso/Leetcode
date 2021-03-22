#
# @lc app=leetcode.cn id=201 lang=python3
#
# [201] 数字范围按位与
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # 因为相邻的两个数必有1~2位不相同的位置，可以找规律：
        # 100100
        # 100101
        # 100110
        # 100111
        # 101000
        # 因为m与n的相同前缀后分别为0，1（SSS0XXX,SSS1XXX）
        # 通过m与n的不断舍取得到相同前缀即可
        count = 0
        while m != n:
            m = m >> 1
            n = n >> 1
            count += 1
        # 得到相同前缀，将末尾0补足
        return m << count
# @lc code=end

