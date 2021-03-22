#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
                # 删除元素可以用nums.pop(i)单个删除，
                # 也可以用del nums[i]一段删除
            else:
                i += 1
        return len(nums)
# @lc code=end

