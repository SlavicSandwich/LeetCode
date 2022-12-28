class Solution:
    def search(self, nums: list[int], target: int) -> int:
        begin = 0
        end = len(nums) -1
        while begin < end:

            mid = (begin + end) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] >= nums[begin]:
                if target < nums[mid] and target >= nums[begin]:
                    end = mid - 1

                else:
                    begin = mid + 1

            elif nums[mid] <= nums[end]:
                if target > nums[mid] and target <= nums[end]:
                    begin = mid + 1

                else:
                    end = mid - 1





        return begin if nums[begin] == target else -1
