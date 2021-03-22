#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        else:
            res, cur, count = [], str(nums[0]), 0
            for i in range(1, len(nums)):
                if (nums[i] - nums[i - 1]) > 1:
                    if count != 0:
                        cur = cur + "->" + str(nums[i - 1])
                    res.append(cur)
                    count = 0
                    cur = str(nums[i])
                else:
                    count += 1
            if count != 0:
                cur = cur + "->" + str(nums[-1])
            res.append(cur)
            return res
# @lc code=end

