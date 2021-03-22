#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            # 在中点右侧是递增情况下
            if nums[mid] < nums[end]:
                if nums[end] >= target and nums[mid] <= target:
                    start = mid
                else:
                    end = mid
            # 中点左侧是递增
            else:
                if nums[start] <= target and nums[mid] >= target:
                    end = mid
                else:
                    start = mid
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1
# @lc code=end

