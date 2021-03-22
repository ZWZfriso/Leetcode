#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        result, iqueue = [], []
        # 队列需要先入队
        iqueue.append(root)
        while len(iqueue) != 0:
            l, temp = len(iqueue), []
            for i in range(0, l):
                cur = iqueue[0]
                iqueue = iqueue[1:]
                temp.append(cur.val)
                if cur.left != None:
                    iqueue.append(cur.left)
                if cur.right != None:
                    iqueue.append(cur.right)
            result.append(temp)
        return result

# @lc code=end

