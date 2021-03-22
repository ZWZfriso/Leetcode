#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # 1.求x和y的异或值。
        # 2.求这个异或值最右位的1
        # 3.找出x和y中是谁造成了这个最右位的1，以分离x和y
        res = 0
        for n in nums:
            res ^= n
        # res = x ^ y
        # 取最右一位的1 
        # lastbit = res & (~res + 1)
        # lastbit = res & (-res)
        lastbit = (res&(res-1))^res
        x = 0
        for n in nums:
            if n & lastbit != 0:
                x ^= n
        return [x, res^x]
# @lc code=end

