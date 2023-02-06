# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hare = head
        tortoise = head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if hare == tortoise:
                return True

        return False

bruh = ListNode(1)
bruh2 = ListNode(2)
bruh3 = ListNode(3)
bruh4 = ListNode(4)
bruh2.next = bruh
bruh.next = bruh2

print(Solution().hasCycle(bruh))