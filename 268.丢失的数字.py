#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        else:
            for i in range(0, len(nums) - 1):
                if nums[i + 1] - nums[i] > 1:
                    return nums[i] + 1
            return nums[-1] + 1
        
# @lc code=end

