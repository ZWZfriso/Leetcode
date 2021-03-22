#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = self.helper(root)
        if res[0] == 0:
            return False
        else:
            return True
    def helper(self, root: TreeNode) -> List[int]:
        # 结果记录，分别为0是否有效，1树的最大值，2树的最小值
        result = []
        if root == None:
            result.append(1)
            result.append(float('-inf'))
            result.append(float('-inf'))
            return result
        # 分治
        left = self.helper(root.left)
        right = self.helper(root.right)
        # 整合：先判定无效情况
        if left[0] == 0 or right[0] == 0:
            result.append(0)
            result.append(float('-inf'))
            result.append(float('-inf'))
            return result
        if left[1] != float('-inf') and left[1] >= root.val:
            result.append(0)
            result.append(float('-inf'))
            result.append(float('-inf'))
            return result
        if right[2] != float('-inf') and right[2] <= root.val:
            result.append(0)
            result.append(float('-inf'))
            result.append(float('-inf'))
            return result
        # 节点为有效时，节点最大值为右子树的最大最，最小值为左子树的最小值
        result.append(1)
        result.append(root.val)
        result.append(root.val)
        if right[1] != float('-inf'):
            result[1] = right[1]
        if left[2] != float('-inf'):
            result[2] = left[2]
        return result
# @lc code=end

