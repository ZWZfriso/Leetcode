#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 不使用额外空间表示不能用哈希表，O(n)表示不能排序
        # 因此，只能使用原本数组的标记和数值记录
        # 观察：a[i]∈[1,n]共n个值，值和索引大小可以相差1
        for i in range(0, len(nums)):
            mark = abs(nums[i]) - 1
            if nums[mark] > 0:
                nums[mark] *= -1
        res = []
        for i in range(0, len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res
# @lc code=end

