#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return head
        point = head
        while point != None:
            node = Node(point.val, point.next)
            point.next = node
            point = node.next
        point = head
        # 很精妙，采用判断前一个节点为非空，来操作空节点
        while point != None:     
            if point.random != None:
                point.next.random = point.random.next
            point = point.next.next
            # -------
            # node = point.random
            # if node != None:
            #     point.random = node.next
            # if point.next != None:
            #     point = point.next.next
            # else:
            #     point = point.next
        point = head.next
        while head != None and head.next != None:
            # 很精妙，采用指针穿线的方法
            node = head.next
            head.next = head.next.next
            head = node
        return point        
# @lc code=end

