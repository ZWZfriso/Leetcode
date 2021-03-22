#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp  = [[0] * (l1 + 1) for _ in range(l2 + 1)]
        for i in range(l2 + 1):
            dp[i][0] = i
        for j in range(l1 + 1):
            dp[0][j] = j
        for i in range(l2):
            for j in range(l1):
                if word2[i] == word1[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i][j])
        return dp[l2][l1]
                    
# @lc code=end

