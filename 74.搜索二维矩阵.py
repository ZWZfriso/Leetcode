#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 先确定行
        if not matrix:
            return False
        start, end, mark = 0, len(matrix) - 1, 0
        while start + 1 < end:
            mid = (start + end) // 2
            temp = matrix[mid]
            if matrix[mid][len(temp)-1] < target:
                start = mid
            else:
                end = mid
        if matrix[start][0] <= target and matrix[start][len(matrix[start]) - 1] >= target:
            mark = start
        elif matrix[end][0] <= target and matrix[end][len(matrix[end]) - 1] >= target:
            mark = end
        else:
            return False
        # 对行找数
        start, end = 0, len(matrix[mark]) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if matrix[mark][mid] < target:
                start = mid
            else:
                end = mid
        if matrix[mark][start] == target or matrix[mark][end] == target:
            return True
        else:
            return False
# @lc code=end

