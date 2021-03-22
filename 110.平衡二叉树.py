#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if self.judge(root) == -1:
            return False
        else:
            return True
    def judge(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left = self.judge(root.left)
        right = self.judge(root.right)

        if left == -1 or right == -1 or left - right > 1 or right - left > 1:
            return -1
        else:
            return left + 1 if left > right else right + 1
# @lc code=end

