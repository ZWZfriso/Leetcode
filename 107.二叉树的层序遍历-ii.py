#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        result, iqueue = [], []
        iqueue.append(root)
        while len(iqueue) > 0:
            temp, l = [], len(iqueue)
            for i in range(0, l):
                cur = iqueue[0]
                iqueue = iqueue[1:]
                temp.append(cur.val)
                if cur.left != None:
                    iqueue.append(cur.left)
                if cur.right != None:
                    iqueue.append(cur.right)
            result.insert(0, temp)
        return result
# @lc code=end

