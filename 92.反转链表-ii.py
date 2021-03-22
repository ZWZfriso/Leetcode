#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head == None or m == n:
            return head
        # 先进行小节点检索
        point = ListNode()
        point.next = head
        head = point
        count = 1
        while count < m:
            head = head.next
            count += 1
        pre, mid = head, head.next
        head = head.next
        last = head
        # 用head作为原始遍历顺序指针，last记录移动的前一个结点
        while count <= n and head != None:
            # 将head指针的下一个记录，将当前节点的指针指向上一个节点
            temp = head.next
            head.next = last
            # 移动上一个节点，并将head指针放在原来的下一个
            last = head
            head = temp
            count += 1
        pre.next = last
        mid.next = head
        return point.next
# @lc code=end

