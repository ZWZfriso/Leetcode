#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        result, iqueue, iturn = [], [], True
        iqueue.append(root)
        while len(iqueue) > 0:
            temp, l = [], len(iqueue)
            for i in range(0, l):
                cur = iqueue[0]
                iqueue = iqueue[1:]
                if iturn:
                    temp.append(cur.val)
                else:
                    temp.insert(0, cur.val)
                if cur.left != None:
                    iqueue.append(cur.left)
                if cur.right != None:
                    iqueue.append(cur.right)
            if iturn:
                iturn = False
            else:
                iturn = True
            result.append(temp)
        return result
# @lc code=end
