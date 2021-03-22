#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # return self.mergeSort(nums)
        # self.quickSort(nums, 0, len(nums) - 1)
        # 构造大顶堆，交换、取头，再交换、取头
        return self.maxStack(nums)

    def maxStack(self, nums:List[int]) -> List[int]:
        # 构造大顶堆，
        l = len(nums) // 2 - 1
        while l >= 0:
            self.maxCheck(nums, len(nums) - 1, l)
            l -= 1
        l = len(nums) - 1
        while l > 0:      
            self.swap(nums, 0, l)  
            l -= 1 
            self.maxCheck(nums, l, 0)
        return nums

    def maxCheck(self, nums:List[int], end:int, idx:int):
        left, right = idx * 2 + 1, idx * 2 + 2
        # 需要比较多次，采用mark记录大值序号的方法
        mark = idx
        if left <= end and nums[left] > nums[mark]:
            mark = left
        if right <= end and nums[right] > nums[mark]:
            mark = right
        if mark != idx:
            self.swap(nums, mark, idx)
            self.maxCheck(nums, end, mark)

        
    def quickSort(self, nums:List[int], start:int, end:int):
        if start < end:
            pivot = self.partition(nums, start, end)
            self.quickSort(nums, start, pivot - 1)
            self.quickSort(nums, pivot + 1, end)
    def partition(self, nums:List[int], start:int, end:int) -> int:
        mark = nums[end]
        i = j = start
        for j in range(start, end):
            if nums[j] < mark:
                self.swap(nums, i, j)
                i += 1
        self.swap(nums, i, end)
        return i
    def swap(self, nums:List[int], i:int, j:int):
        temp = nums[j]
        nums[j] = nums[i]
        nums[i] = temp

    def mergeSort(self, nums:List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        return self.mergeTwo(left, right)

    def mergeTwo(self, left:List[int], right:List[int]) -> List[int]:
        res = []
        l, r = 0, 0
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1
        if l < len(left):
            res.extend(left[l:])
        if r < len(right):
            res.extend(right[r:])
        return res        

# @lc code=end

