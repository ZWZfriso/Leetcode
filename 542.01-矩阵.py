#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#

# @lc code=start
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # 根据广度优先搜索，从外部向内包围
        if not matrix:
            return matrix
        row, col = len(matrix), len(matrix[0])
        iqueue = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    iqueue.append([i,j])
                else:
                    matrix[i][j] = -1
        while len(iqueue) != 0:
            point_i, point_j = iqueue[0][0], iqueue[0][1]
            iqueue = iqueue[1:]
            newpoint = [[point_i-1, point_j], [point_i+1, point_j], [point_i, point_j-1], [point_i, point_j+1]]
            for n in newpoint:
                ii, jj = n[0], n[1]
                if ii >= 0 and ii < row and jj >= 0 and jj < col and matrix[ii][jj] == -1:
                    matrix[ii][jj] = matrix[point_i][point_j] + 1
                    iqueue.append([ii, jj])
        return matrix
                
# @lc code=end

