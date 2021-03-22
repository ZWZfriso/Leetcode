#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        '''
        prenode = ListNode(0)
        prenode.next = head
        pre = prenode
        while pre.next != None and pre.next.next != None:
            # 交换point与point.next节点
            # 将pre-node-nextnode交换成pre-nextnode-node
            node, nextnode = pre.next, pre.next.next
            pre.next = nextnode
            node.next = nextnode.next
            nextnode.next = node
            # 右移
            pre = node
        return prenode.next
        '''
        if head == None or head.next == None:
            return head
        # 记录 head.next.next 作为下一次起始
        # head-head.next 变为 head.next-head 
        nextnode = head.next.next
        node = head.next
        # 交换两点，选出交换后的头、尾
        # 头node返回，尾递归
        node.next = head
        head.next = self.swapPairs(nextnode)     
        return node
# @lc code=end

