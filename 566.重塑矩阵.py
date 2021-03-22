#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        lens, record = 0, []
        for num in nums:
            lens += len(num)
            record.extend(num)
        if lens != r * c:
            return nums
        res = []
        for i in range(0, r):
            temp = []
            for j in range(0, c):
                temp.append(record.pop(0))
            # 注意append和extend区别，append是追加元素，extend是增加表长
            res.append(temp)

        return res
        
# @lc code=end

