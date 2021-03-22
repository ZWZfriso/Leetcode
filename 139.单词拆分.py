#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] = true 表示从0~i正好能覆盖
        # dp[i] = s[:i+1] in wordDict 
        # 或 dp[i] = dp[j] and s[j+1:i+1] in word Dict
        # 初始值dp[i] = false
        # 返回值dp[n-1]
        n = len(s)
        dp = [False for _ in range(n)]
        for i in range(n):
            if s[:i + 1] in wordDict:
                dp[i] = True
            else:
                for j in range(i):
                    if dp[j] and s[j + 1: i + 1] in wordDict:
                        dp[i] = True
        return dp[n - 1]

# @lc code=end

