#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, cur = 0, 0
        for num in nums:
            if num == 0:
                res = cur if cur > res else res
                cur = 0
            else:
                cur += 1
        res = cur if cur > res else res
        return res
# @lc code=end

