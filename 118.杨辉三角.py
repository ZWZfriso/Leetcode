#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        if numRows == 1:
            return [[1]]
        resList = [[1], [1, 1]]
        newList = []
        for i in range(2, numRows):
            lastList = resList[-1]
            newList = [] #重新赋值，用clear的话会把append后的值也改变
            newList.append(1)
            for i in range(0, len(lastList) - 1):
                newList.append(lastList[i] + lastList[i+1])
            newList.append(1)
            resList.append(newList)
        return resList
# @lc code=end

