class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        allsum = 0
        contains = False
        for i in nums:
            if i != 0:
                allsum = allsum * i if allsum != 0 else i
            elif not contains and i == 0:
                contains = True

            elif contains and i == 0:
                allsum = 0
                break
        for k in range(len(nums)):
            if nums[k] != 0 and contains:
                nums[k] = 0

            elif nums[k] != 0 and not contains:
                nums[k] = allsum // nums[k]

            elif nums[k] == 0 and contains:
                nums[k] = allsum

        return nums