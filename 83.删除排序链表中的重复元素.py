#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        last, point = head.val, head
        while point.next != None:
            cur = point.next
            if cur.val == last:
                point.next = cur.next
            else:
                last = cur.val
                point = cur
        return head
        '''
        point = head
        while point != None:
            while point.next != None and point.val == point.next.val:
                point.next = point.next.next
            point = point.next
        return head
        '''
# @lc code=end

