#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        res, l = [], len(triangle)
        if l == 0:
            return 0
        for tri in triangle:
            temp = []
            for t in tri:
                temp.append(t)
            res.append(temp)
        '''
        # 获取倒数第二行的坐标
        l -= 2
        while l >= 0:
            for i in range(0, len(triangle[l])):
                res[l][i] += min(res[l + 1][i], res[l + 1][i + 1])
            l -= 1
        return res[0][0]
        '''
        for i in range(1, l):
            t = len(triangle[i])
            for j in range(0, t):
                if j > 0 and j < len(triangle[i - 1]):
                    res[i][j] += min(res[i - 1][j - 1], res[i - 1][j])
                elif j > 0:
                    res[i][j] += res[i - 1][j - 1]
                else:
                    res[i][j] += res[i - 1][j]
        return min(res[l - 1])                
# @lc code=end

