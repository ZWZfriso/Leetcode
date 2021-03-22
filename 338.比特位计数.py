#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        result = []
        for i in range(num + 1):
            n, count = i, 0
            while n != 0:
                if n & (-n) == 1:
                    count += 1
                n = n >> 1
            result.append(count)
        return result
# @lc code=end

