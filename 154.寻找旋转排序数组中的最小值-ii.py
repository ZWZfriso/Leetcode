#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 一般情况和无重复一样，中点与最右值比较，再移动端点
        # 有重复值需要考虑222221222的情况：
        # 此时最右与中点一样，无法判断情况，谨慎考虑：移动端点
        if not nums:
            return 0
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid
            elif nums[mid] < nums[end]:
                end = mid
            else:
                end -= 1
        if nums[start] < nums[end]:
            return nums[start]
        else:
            return nums[end]
# @lc code=end

