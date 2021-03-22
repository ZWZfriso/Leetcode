    def backPackII(self, m, A, V):
        # write your code here
        # dp[i][j]表示前i个物品，容量是否能为j
        # dp[i][j] = dp[i-1][j] 不装第i个物品的容量
        # 或者 dp[i][j] = dp[i-1][j-a[i]] 装第i个物品
        # 初始值dp[0][0] = 0
        n, dp = len(A), []
        for i in range(n + 1):
            temp = []
            for j in range(m + 1):
                temp.append(0)
            dp.append(temp)
        # i、j表示第i个物品，j+1表示真实容量
        for i in range(n):
            for j in range(m):
                dp[i + 1][j + 1] = dp[i][j + 1]
                if A[i] <= j + 1:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i][j + 1 - A[i]] + V[i])
        return dp[n][m]


        