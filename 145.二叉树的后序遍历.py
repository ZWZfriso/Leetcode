#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        result, istack, lastnode = [], [], None
        while root != None or len(istack) != 0:
            while root != None:
                istack.append(root)
                root = root.left
            cur = istack[-1]
            if cur.right == None or cur.right == lastnode:
                istack = istack[:-1]
                result.append(cur.val)
                lastnode = cur
            else:
                root = cur.right
        return result
# @lc code=end

