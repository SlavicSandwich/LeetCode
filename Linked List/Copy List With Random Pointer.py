"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        to_copy = {None:None}
        itero = head
        while itero:
            to_copy[itero]= Node(itero.val)
            itero = itero.next

        for orig in to_copy:
            if not orig: continue
            to_copy[orig].random = to_copy[orig.random if orig else None]
            to_copy[orig].next = to_copy[orig.next if orig else None]

        return to_copy[head]


bruh = Node(1)
bruh2 = Node(2)
bruh.next=  bruh2
bruh3 = Node(3)
bruh2.next = bruh3
bruh.random = None
bruh2.random = bruh
bruh3.random = bruh2

Solution().copyRandomList(bruh)