#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        result, pre = ListNode(), ListNode()
        pre.next = head
        bigger, head = result, pre
        while head.next != None:
            if head.next.val < x:
                head = head.next
            else:
                node = head.next
                head.next = node.next
                bigger.next = node
                bigger = bigger.next
        bigger.next = None
        head.next = result.next
        return pre.next
# @lc code=end

