# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return head.next
        l = head

        r = head
        for k in range(1, n):
            r = r.next

        prev = ListNode(-1)
        prev.next = head
        while True:
            r = r.next
            if not r:
                prev.next = prev.next.next
                return head if prev.val != -1 else prev.next
            prev = l
            l = l.next




list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
list.next.next.next = ListNode(4)
list.next.next.next.next = ListNode(5)


bruv = Solution().removeNthFromEnd(list, 2)
while bruv:
    print(bruv.val)
    bruv= bruv.next

