#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once, twice = 0, 0
        # n,once,twice 
        # 0 0 0 
        # 0 1 0 
        # 0 0 1
        # 1 0 0
        # 1 1 0 
        # 1 0 1
        # 对于n=1而言，3个1最终仍使once=0，实现3个数的位运算保证 
        for n in nums:
            once = once ^ n & ~twice 
            twice = twice ^ n & ~once
        return once
# @lc code=end

