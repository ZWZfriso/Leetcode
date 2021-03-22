#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre = ListNode()
        pre.next = head
        head, last = pre, float('inf')
        # 删除重复的额外点，只需要一个指针滑动，判断当前点和下一点(如有)；
        # 而删除全部重复点，则需要空指针领头，进行领头后续两个节点的判断(无两个节点则无需判断)。
        while head.next != None and head.next.next != None:
            if head.next.val == head.next.next.val:
                last = head.next.val
                while head.next != None and head.next.val == last:
                    head.next = head.next.next
            else:
                head = head.next
        return pre.next
# @lc code=end

