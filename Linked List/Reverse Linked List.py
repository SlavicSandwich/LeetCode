
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        curhead = head
        nexxt = None
        tmpnext = curhead.next
        while curhead:
            curhead.next, curhead, nexxt = nexxt, tmpnext, curhead
            if tmpnext:
                tmpnext = curhead.next
            else:
                return nexxt




head = ListNode(1)
head.next= ListNode(2)

# head = ListNode(1)
# head.next = (ListNode(2))
# head.next.next = (ListNode(3))
# head.next.next.next = (ListNode(4))
# head.next.next.next.next = (ListNode(5))
bruv = Solution().reverseList()
while bruv:
    print(bruv.val)
    bruv= bruv.next

