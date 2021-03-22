#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # 最大和：左/右子树最大和，左右子树加根节点的最大和
        summax = self.find(root)
        return summax[1]

    def find(self, root: TreeNode) -> List[int]:
        if root == None:
            return [0, float('-inf')]
        # 分治
        left = self.find(root.left)
        right = self.find(root.right)
        result = []
        # 合并规整，先求单边值，再求最大和
        if left[0] > right[0]:
            result.append(max(left[0] + root.val, 0))
        else:
            result.append(max(right[0] + root.val, 0))
        result.append(max(max(left[1], right[1]), (left[0] + right[0] + root.val)))
        return result
# @lc code=end

