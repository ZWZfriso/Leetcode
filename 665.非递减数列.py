#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        mark = 0
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                mark += 1
                # 当前点大于右点，存在两种可解情况：
                # 1. 当前点变化【2，2，3，2，4】
                # 2. 右点变化【2，3，3，2，4】
                if i >= 1:
                    if nums[i+1] >= nums[i-1]:
                        nums[i] = nums[i-1]
                    else:
                        nums[i+1] = nums[i]
            if mark > 1:
                return False
        return True
# @lc code=end

