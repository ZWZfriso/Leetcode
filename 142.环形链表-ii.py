#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        # 相交点时，快慢指针分别走过a+b,a+n(b+c),c表示环剩下的长度;
        # 得2(a+b)=a+n(b+c),即a=c+(n-1)(b+c),表示a的长度为n-1圈的环+c;
        # 而慢指针继续走c即可回到入环点，再经过n-1圈仍然在入环点;
        slow, fast = head, head.next
        while fast != None and fast.next != None:
            if fast == slow:
                fast = head
                # 因为一开始fast=head.next，此时slow.next才是真当前点
                slow = slow.next
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
            fast = fast.next.next
            slow = slow.next
        return None
# @lc code=end

