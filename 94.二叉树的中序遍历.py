#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        result, istack = [], []
        while root != None or len(istack) != 0:
            while root != None:
                istack.append(root)
                root = root.left
            cur = istack[-1]
            result.append(cur.val)
            istack = istack[:-1]
            root = cur.right
        return result
# @lc code=end

