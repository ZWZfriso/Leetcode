#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        # 按规则扫描
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == "1" and self.dfs(grid, i, j) >= 1:
                    count += 1
        return count
    def dfs(self, grid: List[List[str]], i: int, j: int) -> int:
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return 0
        if grid[i][j] == "1":
            grid[i][j] = "0"
            # 将grid列表传入函数属于引用传递，访问后改值相当于列表自带访问记录功能
            return self.dfs(grid, i-1, j) + self.dfs(grid, i, j-1) +\
                self.dfs(grid, i+1, j) + self.dfs(grid, i, j+1) + 1
        return 0
# @lc code=end

