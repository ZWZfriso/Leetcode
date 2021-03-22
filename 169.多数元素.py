#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        line = len(nums) // 2
        record = {}
        for num in nums:
            if record.get(num) == None:
                record[num] = 1
            else:
                record[num] = record[num] + 1
        for key, value in record.items():
            if value > line:
                return key
        return 0

# @lc code=end

