"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        nodeMap = dict()
        while(curr):
            nodeMap[curr] = Node(curr.val)
            curr = curr.next
        
        for node in nodeMap:
            if(node.next):
                nodeMap[node].next =  nodeMap[node.next]
            if(node.random):
                nodeMap[node].random = nodeMap[node.random]
        
        if(head):
            return nodeMap[head]
        else:
            return None

