#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 1.采用宽度法，选取左右点固定区间，直接取高度，O(n2)
        # 2.采用高度法，对于每根柱子求取最大宽度
        # 固定高度，求宽度，即找左右侧：
        # 左侧比当前高度低的第一根柱子;右侧比当前高度低的第一根柱子
        # 在矩形中加入左右哨兵以求宽度
        heights = [0] + heights + [0]
        res, istack = 0, []
        for i in range(len(heights)):
            # 每次入栈，必须保证矩形高度为递增的
            while istack and heights[istack[-1]] > heights[i]:
                last= istack.pop()
                res = max(res, heights[last]*(i - 1 - istack[-1]))
            istack.append(i)
        return res
# @lc code=end

