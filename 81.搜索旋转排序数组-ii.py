#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start, end, mark = 0, len(nums) - 1, -1
        while start + 1 < end:
            mid = (start + end) // 2
            # 有重复的旋转数组中存在3种情况
            # 当中点小于右点，说明中点右侧是递增的
            if nums[mid] < nums[end]:
                if nums[mid] <= target and nums[end] >= target:
                    start = mid
                else:
                    end = mid
            # 当中点大于右点，说明中点左侧的递增的
            elif nums[mid] > nums[end]:
                if nums[start] <= target and nums[mid] >= target:
                    end = mid
                else:
                    start = mid
            # 当中点等于右点时，无法判定哪侧递增2222122
            else:
                if nums[end] == target:
                    mark = end
                    break
                else:
                    end -= 1
        if mark != -1 or nums[start] == target or nums[end] == target:
            return True
        else:
            return False        
# @lc code=end

