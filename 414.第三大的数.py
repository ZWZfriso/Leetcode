#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = max2 = max3 = float('-inf')
        for i in range(0, len(nums)):
            # 为防止重复数字的影响，在判断时多添加一个
            # 【">"->">"和"<"】
            if nums[i] > max3:
                if nums[i] < max2:
                    max3 = nums[i]
                elif nums[i] > max2:
                    if nums[i] < max1:
                        max3 = max2
                        max2 = nums[i]
                    elif nums[i] > max1:
                        max3 = max2
                        max2 = max1
                        max1 = nums[i]
        if max3 == float('-inf'):
            return max1 
        else:
            return max3
# @lc code=end

