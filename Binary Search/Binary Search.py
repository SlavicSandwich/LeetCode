class Solution:
    def search(self, nums: list[int], target: int) -> int:
        begin = 0
        end = len(nums) - 1
        while begin < end:
            mid = (begin + end) // 2
            if target < nums[mid]:
                end = mid

            elif target > nums[mid]:
                begin = mid + 1

            else:
                return mid

        if nums[begin] == target:
            return begin

        return -1

print(Solution().search([0], 0))
print(Solution().search([0, 1], 1))
print(Solution().search([-1, 0, 3, 9, 12], 0))
