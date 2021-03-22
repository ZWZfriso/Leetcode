#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        dp, m, n = [], len(obstacleGrid), len(obstacleGrid[0])
        for i in range(0, m):
            temp = []
            for j in range(0, n):
                temp.append(1)
            dp.append(temp)
        i, j = 1, 1
        # 处理[[0,0],[1,1],[0,0]]的数组，设置好左侧与上侧
        while i < m:
            if obstacleGrid[i][0] == 1 or dp[i - 1][0] == 0:
                dp[i][0] = 0
            i += 1
        while j < n:
            if obstacleGrid[0][j] == 1 or dp[0][j - 1] == 0:
                dp[0][j] = 0
            j += 1
        print(dp)
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
# @lc code=end

