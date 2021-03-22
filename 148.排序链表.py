#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return self.mergeSort(head)

    def findMiddle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def mergeTwo(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre = ListNode()
        point = pre
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
            point = point.next
        if l1 != None:
            point.next = l1
        if l2 != None:
            point.next = l2
        return pre.next

    def mergeSort(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        mid = self.findMiddle(head)
        last = mid.next
        mid.next = None
        left = self.mergeSort(head)
        right = self.mergeSort(last)
        return self.mergeTwo(left, right)
# @lc code=end

