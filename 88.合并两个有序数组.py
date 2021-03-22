#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 在判断m和n时，需要判别m与n的关键性
        # nums2的关键点>nums1，理由为它是添加的核心，无它则该操作无意义
        if n == 0:
            pass
        elif m == 0:
            nums1[:n]=nums2[:n]
        else:
            # 与普通数组合并不同的是，此次是添加至数组1上
            # 需要确定原数组的数字是否遍历完毕，故添加k做原数组计数用
            i, j, k = 0, 0, 0 
            while k < m and j < n:
                if nums1[i] < nums2[j]:
                    i += 1
                    k += 1
                    continue
                # 添加=的原因是保持判等空间闭合
                if nums2[j] <= nums1[i]:
                    nums1.insert(i, nums2[j])
                    nums1.pop()
                    j += 1
                    i += 1
                    continue
            if j < n:
                nums1[m + j:] = nums2[j:]

# @lc code=end

