#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = mark = sum(nums[0:k])/k
        for i in range(k, len(nums)):
            mark = (mark * k + nums[i] - nums[i - k])/k
            if mark > res:
                res = mark
        return res
        '''
        if k == len(nums):
            return sum(nums)/len(nums)
        else:
            res = float('-inf')
            for i in range(k, len(nums) + 1):
                temp = sum(nums[(i - k):i]) / k
                if temp > res:
                    res = temp
            return res
        '''
# @lc code=end

