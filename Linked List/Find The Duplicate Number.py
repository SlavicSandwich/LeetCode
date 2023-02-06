class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        fast = 0
        slow = 0
        while True:

            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow





# print(Solution().findDuplicate([1,1,2]))
# print(Solution().findDuplicate([1,3,4,2,2]))
print(Solution().findDuplicate([3,1,3,4,2]))