#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # 考虑负数的话，将最小的值也记录
        big1 = big2 = big3 = float('-inf')
        sma1 = sma2 = float('inf')
        for num in nums:
            if num > big3:                    
                big3 = num
                if num > big2:
                    big3 = big2
                    if num > big1:
                        big2 = big1
                        big1 = num
                    else:
                        big2 = num
            if num < sma2:
                sma2 = num
                if num < sma1:
                    sma2 = sma1
                    sma1 = num               
        return max(big1*big2*big3, big1*sma1*sma2)
# @lc code=end

