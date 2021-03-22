#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = 0
        for digit in digits:
            sum *= 10
            sum += digit
        if sum == 0:
            digits[-1] = 1
            return digits

        sum += 1
        res = []
        while sum != 0:
            res.insert(0, sum%10)
            sum = sum // 10
        return res
        '''
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits)-1-i))
        return [int(i) for i in str(num+1)]
        '''
# @lc code=end

