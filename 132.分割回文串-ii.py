#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#

# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # 预处理子串是否回文
        ispali = [[False] * n for _ in range(n)]
        for l in range(n):
            for i in range(n):
                j = i + l
                if j >= n:
                    break
                # 跨度为0，表示1个字符
                if l == 0: 
                    ispali[i][j] = True
                # 跨度为1，表示2个字符
                elif l == 1:
                    ispali[i][j] = (s[i] == s[j])
                else:
                    ispali[i][j] = (s[i] == s[j] and ispali[i + 1][j - 1])
        # 分割次数计算：
        # 1.回文，分割为0;
        # 2.不回文，则j~i回文(0<j<i)，得dp[j] + 1.
        dp = [i for i in range(n)]
        for i in range(n):
            if ispali[0][i]:
                dp[i] = 0
            else:
                dp[i] = min([dp[j] + 1 for j in range(i) if ispali[j + 1][i]])
        return dp[n - 1]      
        
# @lc code=end

