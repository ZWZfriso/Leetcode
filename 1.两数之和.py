#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        length = len(nums)
        # use number for representation
        for i in range(0, length):
            j = i + 1
            while j < length:
                if target == nums[i] + nums[j]:
                    return [i, j]
                else:
                    j += 1
        return NULL


# @lc code=end

