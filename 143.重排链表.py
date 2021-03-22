#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 思路：从中间破开链表，反转后链再合并
        if head == None or head.next == None:
            return head
        mid = self.findMiddle(head)
        last = self.reverseList(mid.next)
        mid.next = None
        head = self.mergeTwo(head, last)

    def findMiddle(self, head: ListNode) -> ListNode:
        slow, fast = head, head.next
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverseList(self, head: ListNode) -> ListNode:
        pre = ListNode()
        pre.next = head
        while head.next != None:
            last = head.next
            head.next = last.next
            last.next = pre.next
            pre.next = last
        return pre.next
    
    def mergeTwo(self, left: ListNode, right: ListNode) -> ListNode:
        pre, isleft = ListNode(), True
        point = pre
        while left != None and right != None:
            if isleft:
                point.next = left
                left = left.next
                isleft = False
            else:
                point.next = right
                right = right.next
                isleft = True
            point = point.next
        if left != None:
            point.next = left
        if right != None:
            point.next = right
        return pre.next
# @lc code=end

