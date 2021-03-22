#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inprice, sumprice = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] < inprice:
                inprice = prices[i]
            elif prices[i] > inprice:
                sumprice += prices[i] - inprice
                inprice = prices[i]
                # 因为不存在买卖间隙
                # 当卖出后，后续的买入判别在当前卖出的位置
        return sumprice
# @lc code=end

