#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        record = {}
        for num in nums:
            if record.get(num):
                return True
            else:
                record[num] = 1
        return False
# @lc code=end

