#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end, mark = 0, len(nums) - 1, -1
        while start <= end:
            mid = int((start + end)/2)
            if nums[mid] == target:
                mark = mid
                break
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        if mark == -1:
            return [-1, -1]
        else:
            start = end = mark
            while end < len(nums):
                if nums[end] != target:
                    break
                end += 1
            while start >= 0:
                if nums[start] != target:
                    break
                start -= 1
            return [start + 1, end - 1]
# @lc code=end

