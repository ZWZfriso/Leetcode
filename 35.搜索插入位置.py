#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        #要先判断target是否在范围内
        if target < nums[0]:
            return 0
        
        left, right = 0, len(nums)
        #循环l<r（最后取的区间会含1个元素）与l<=r（最后区间元素为空）
        while left < right:
            #严格限制了mid的计算结果为整型
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid            
        return left
        '''
        start, end, mark = 0, len(nums) - 1, 0
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        print(start, end)
        if nums[start] >= target:
            mark = start
        elif nums[end] >= target:
            mark = end
        else:
            mark = end + 1
        return mark   
# @lc code=end

