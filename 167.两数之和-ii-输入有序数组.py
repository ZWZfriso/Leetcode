#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) <= 1:
            return []
        '''     # 循环过多
        point, i= 0, 1
        while point < len(numbers) and i < len(numbers):
            if numbers[point] + numbers[i] == target:
                return [point + 1, i + 1]
            elif numbers[point] + numbers[i] > target:
                point += 1
                i = point + 1
            else:
                i += 1
        return []
        '''
        # 用双指针，缩减搜索空间，关键是【i < j】
        i, j = 0, len(numbers)-1
        while i < j:
            now = numbers[i] + numbers[j]
            if now < target:
                i += 1
            elif now > target:
                j -= 1
            else:
                return [i + 1, j + 1]
        return []

# @lc code=end

