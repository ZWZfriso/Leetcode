#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        else:
            # 记录买入价格即可
            # 区别于求和，求和需要记录前一个位置的最大和
            inprice, maxprice = prices[0], 0
            for i in range(1, len(prices)):
                if prices[i] < inprice:
                    inprice = prices[i]
                elif prices[i] > inprice and maxprice < (prices[i] - inprice):
                    maxprice = prices[i] - inprice
                else:
                    pass
            return maxprice

# @lc code=end

