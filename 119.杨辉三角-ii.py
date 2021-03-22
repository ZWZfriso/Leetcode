#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []
        elif rowIndex == 0:
            return [1]
        else:
            curList = [1, 1]
            for i in range(1, rowIndex):
                newList = []
                newList.append(1)
                for i in range(0, len(curList) - 1):
                    newList.append(curList[i] + curList[i+1])
                newList.append(1)
                curList = newList
            return curList
# @lc code=end

