#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        end, maxidx, step = 0, 0, 0
        # 假设你总是可以到达数组的最后一个位置。
        # 在遍历数组时，不访问最后一个元素，
        # 因为在访问最后一个元素之前，边界一定大于等于最后一个位置
        # 如果访问最后一个元素，在边界正好为最后一个位置的情况下
        # 会增加一次「不必要的跳跃次数」
        for i in range(0, n - 1):
            maxidx = max(maxidx, i + nums[i])
            # 遇到边界则更新边界
            if i == end:
                end = maxidx
                step += 1
        return step      
                                
# @lc code=end

