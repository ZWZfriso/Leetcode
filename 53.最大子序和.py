#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ''' 
        max, cur = -999999999999, 0
        for num in nums:
            if cur >= 0:
                cur += num
            else:
                cur = num
            if cur > max:
                max = cur
        return max
        '''
        if not nums:
            return 0
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            # 每一次寻找都是子段的比较，前面连续的子段值是否加上当前值 
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
        return maxSum
# @lc code=end

