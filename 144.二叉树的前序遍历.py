#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        result, istack = [], []
        while root != None or len(istack) != 0:
            while root != None:
                result.append(root.val)
                istack.append(root)
                root=root.left
            root = istack[-1]
            istack = istack[:-1]
            root = root.right
        return result
# @lc code=end

