#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # 采用记录两侧坐标和度数的法则法则 
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1
        res = len(nums)
        mindegree = max(count.values())
        for x in count:
            if count[x] == mindegree:
                res = min(res, right[x]-left[x] + 1)
        return res
# @lc code=end

