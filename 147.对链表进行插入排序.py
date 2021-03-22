#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre = ListNode()
        pre.next = head
        point = head
        while point.next != None:
            node = point.next
            if point.val <= node.val:
                point = point.next
                continue
            else:
                point.next = node.next
                po = pre
                while po.next != None and po.next.val < node.val:
                    po = po.next
                node.next = po.next
                po.next = node       
        return pre.next

# @lc code=end

