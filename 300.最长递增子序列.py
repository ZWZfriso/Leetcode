#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i]表示从0~i最长递增序列的长度
        # dp[i] = max(dp[j]) + 1, if nums[i]>nums[j]
        # 初始值dp[i] = 1
        # 返回值max(dp[i])
        n = len(nums)
        dp = [1 for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
# @lc code=end

