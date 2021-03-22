#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True
        slow, fast = head, head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        last = self.reverseList(slow.next)    
        slow.next = None 
        while last != None and head != None:
            if last.val != head.val:
                return False
            last, head = last.next, head.next
        return True  

    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        pre = ListNode()
        # 切记，在反转链表时，空指针不需要head辅助
        pre.next = head
        while head.next != None:
            node = head.next
            head.next = node.next
            node.next = pre.next
            pre.next = node
        return pre.next
# @lc code=end

