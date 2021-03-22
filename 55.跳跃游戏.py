#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp[i]表示能否从0跳到i
        if not nums:
            return True
        maxlen = nums[0]
        for i in range(1, len(nums)):
            if i <= maxlen:
                maxlen = max(maxlen, i + nums[i])
        # 保证可到的最大长度大于等于数组长度，且[0]能通过
        if maxlen >= len(nums) - 1:
            return True
        else:
            return False
# @lc code=end

