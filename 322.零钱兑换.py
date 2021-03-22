#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i]表示总金额为i的时候，硬币个数
        dp = [(amount + 1) for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if (i - c) >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        for i in range(amount + 1):
            if dp[i] == amount + 1:
                dp[i] = -1
        return dp[amount]

# @lc code=end

