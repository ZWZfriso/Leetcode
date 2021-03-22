#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        record = {}
        for i in range(0, len(nums)):
            find = record.get(nums[i])
            # find 没找到是None，找到是其值，其值可能为0，故而要详判断
            if find != None and (i - record[nums[i]]) <= k:
                return True
            else:
                record[nums[i]] = i
        return False
# @lc code=end

