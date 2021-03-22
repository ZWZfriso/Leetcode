#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        if l1 == 0 or l2 == 0:
            return 0
        dp = []
        for i in range(l2 + 1):
            temp = []
            for j in range(l1 + 1):
                temp.append(0)
            dp.append(temp)

        for i in range(l2):
            for j in range(l1):
                if text2[i] == text1[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        
        return dp[l2][l1]

# @lc code=end

