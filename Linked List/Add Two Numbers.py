# Definition for singly-linked list.
class LN:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: LN, l2: LN) -> LN:
        head = LN(0)
        dummy = head
        pointer1 = l1
        pointer2 = l2
        diff = 0
        while pointer1 and pointer2:
            res = pointer1.val + pointer2.val + diff
            if res >= 10:
                diff = 1
                res = res - 10

            else:
                diff = 0
            dummy.val = dummy.val + res
            pointer1 = pointer1.next
            pointer2 = pointer2.next
            if pointer1 or pointer2:
                dummy.next = LN(0)
                dummy = dummy.next

        while pointer1:
            res = diff + pointer1.val

            if res >= 10:
                diff = 1
                res = res - 10
            else:
                diff = 0
            dummy.val = res
            if pointer1.next:
                dummy.next = LN()
                dummy = dummy.next
                pointer1 = pointer1.next

            else:
                break

        while pointer2:
            res = diff + pointer2.val

            if res >= 10:
                diff = 1
                res = res - 10
            else:
                diff = 0
            dummy.val = res

            if pointer2.next:
                dummy.next = LN()
                dummy = dummy.next
                pointer2 = pointer2.next
            else:
                break

        if diff:
            dummy.next = LN(1)
        return head




list1 = LN(3)
list1.next = LN(7)
# list1.next.next = LN(3)
#
#
list2 = LN(9)
list2.next = LN(2)
# list2.next.next = LN(4)
# # list2.next.next.next = LN(1)

bruv = Solution().addTwoNumbers(list1, list2)
while bruv:
    print(bruv.val)
    bruv= bruv.next
