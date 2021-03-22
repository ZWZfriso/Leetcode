#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        '''# O(n)
        res = []
        for r in s:
            res.insert(0, r)
        for i in range(len(res)):
            s[i] = res[i]
        '''
        # O(n) 双指针
        l, r = 0, len(s) - 1
        while l < r:
            temp = s[r]
            s[r] = s[l]
            s[l] = temp
            l += 1
            r -= 1
        
# @lc code=end

