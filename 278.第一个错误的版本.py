#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        start, end = 0, n
        while start + 1 < end:
            mid = (start + end) // 2
            # 等于false表示当前是正确的，错误的在后面
            if isBadVersion(mid) == False:
                start = mid
            else:
                end = mid
        if isBadVersion(start):
            return start
        else:
            return end           
# @lc code=end

