#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for i in range(0, m):
            temp = []
            for j in range(0, n):
                temp.append(1)
            dp.append(temp)
        # 因为机器人往右下路线固定
        # 左侧与上侧的的值都仅有1条路线
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
# @lc code=end

