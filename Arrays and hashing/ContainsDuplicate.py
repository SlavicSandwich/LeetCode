class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        getlen = len(nums)
        nums = set(nums)
        if getlen != len(nums):
            return True

        else:
            return False