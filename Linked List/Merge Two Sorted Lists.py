# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1 and not list2:
            return list1

        if not list1:
            return list2

        if not list2:
            return list1

        pointer1 = list1
        pointer2 = list2
        if pointer1.val <= pointer2.val:
            newone = ListNode(pointer1.val)
            pointer1 = pointer1.next

        else:
            newone = ListNode(pointer2.val)
            pointer2 = pointer2.next

        itero = newone

        while pointer1 and pointer2:
            if pointer1.val <= pointer2.val:
                itero.next = ListNode(pointer1.val)
                pointer1 = pointer1.next
                itero = itero.next

            elif pointer1.val > pointer2.val:
                itero.next = ListNode(pointer2.val)
                pointer2 = pointer2.next
                itero = itero.next

        while pointer1:
            itero.next = ListNode(pointer1.val)
            pointer1 = pointer1.next
            itero = itero.next

        while pointer2:
            itero.next = ListNode(pointer2.val)
            pointer2 = pointer2.next
            itero = itero.next

        return newone
list1 = ListNode(-10)
list1.next = ListNode(-9)
list1.next.next = ListNode(-6)
list1.next.next.next = ListNode(-4)
list1.next.next.next.next = ListNode(1)
list1.next.next.next.next.next = ListNode(9)
list1.next.next.next.next.next.next = ListNode(9)

list2 = ListNode(-5)
list2.next = ListNode(-3)
list2.next.next = ListNode(0)
list2.next.next.next = ListNode(7)
list2.next.next.next.next = ListNode(8)
list2.next.next.next.next.next = ListNode(8)

# list1 = ListNode(-9)
# list1.next = ListNode(3)
#
# list2 = ListNode(5)
# list2.next = ListNode(7)


# list1 = ListNode(2)
# list2 = ListNode(1)

# list1 = ListNode(1)
# list1.next = ListNode(2)
# list1.next.next = ListNode(4)
# list1.next.next.next = ListNode(4)
# #
# list1.next.next.next.next = ListNode(5)
#
# list2 = ListNode(1)
# list2.next = ListNode(3)
# list2.next.next = ListNode(4)
#
bruv = Solution().mergeTwoLists(list1, list2)

while bruv:
    print(bruv.val)
    bruv= bruv.next
