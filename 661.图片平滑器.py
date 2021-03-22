#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#

# @lc code=start
import math
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        ro = len(M)
        co = len(M[0])
        res = [[0] * co for row in range(ro)]
        print(res)
        for i in range(0, ro):
            for j in range(0, co):
                temp, count = 0, 1
                if i == 0 or i == ro - 1 or j == 0 or j == co - 1:
                    temp += M[i][j]
                    # 上下左右
                    u, d, l, r = i-1, i+1, j-1, j+1
                    if u >= 0:
                        temp += M[u][j]
                        count += 1
                        if l >= 0:
                            temp += M[u][l]
                            count += 1 
                        if r < co:
                            temp += M[u][r]
                            count += 1 
                    if d < ro:
                        temp += M[d][j]
                        count += 1
                        if l >= 0:
                            temp += M[d][l]
                            count += 1 
                        if r < co:
                            temp += M[d][r]
                            count += 1                      
                    if l >= 0:       
                        temp += M[i][l]
                        count += 1 
                    if r < co:
                        temp += M[i][r]
                        count += 1 
                    res[i][j] = math.floor(temp / count)
                else:
                    temp += M[i-1][j-1] + M[i-1][j] + M[i-1][j+1] 
                    temp += M[i][j-1] + M[i][j] + M[i][j+1]
                    temp += M[i+1][j-1] + M[i+1][j] + M[i+1][j+1]
                    res[i][j] = math.floor(temp / 9)
        return res
        
# @lc code=end