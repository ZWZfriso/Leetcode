#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #双指针
        i, j = 0, 1
        while j < len(nums):
            if nums[i] == nums[j]:
                nums.pop(j)
            else:
                i+=1
                j=i+1
# @lc code=end

