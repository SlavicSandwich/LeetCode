# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        nexxt = None

        tmpnext = second.next
        while second:
            second.next, second, nexxt = nexxt, tmpnext, second
            if tmpnext:
                tmpnext = second.next
        second = nexxt

        tail = head
        while tail and second:
            tmp = tail.next
            tail.next = ListNode(second.val)
            tail.next.next = tmp
            tail = tail.next.next
            second = second.next





list = ListNode(1)
# list.next = ListNode(2)
# list.next.next = ListNode(3)
# list.next.next.next = ListNode(4)
# list.next.next.next.next = ListNode(5)

Solution().reorderList(list)



