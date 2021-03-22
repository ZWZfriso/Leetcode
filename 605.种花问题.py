#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prehave = False
        for i in range(0, len(flowerbed) - 1):
            # 捋逻辑：当前点已有，直接标记true；
            # 无花则判断是否可种，可则标记true；不可则标记false。
            if flowerbed[i] != 1:
                if not prehave and flowerbed[i + 1] == 0:
                    prehave = True
                    n -= 1
                    continue
                prehave = False
            else:
                prehave = True
        if not prehave and flowerbed[-1] == 0:
            n -= 1
        if n <= 0:
            return True
        else:
            return False 

# @lc code=end

