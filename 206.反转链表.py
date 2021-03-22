#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = ListNode()
        pre.next = head
        while head.next != None:
            # 记录下一个节点
            last = head.next
            # 将当前节点next指向下一个节点的next
            head.next = last.next
            # 下一个节点next指向空指针next
            last.next = pre.next
            # 将空指针移动至最左
            pre.next = last
        return pre.next

# @lc code=end

