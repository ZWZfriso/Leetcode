#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # 关键点:用visited记录新建的节点，以连接
        visited = {}
        return self.cloneg(node, visited)

    def cloneg(self, node: 'Node', visited: dict) -> 'Node':
        if node == None:
            return node
        if visited.get(node) != None:
            return visited[node]
        newnode = Node(node.val, [])
        visited[node] = newnode
        for n in range(0, len(node.neighbors)):
            newnode.neighbors.append(self.cloneg(node.neighbors[n], visited))
        return newnode
# @lc code=end

