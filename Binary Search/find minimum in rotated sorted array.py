def check_neighbours(nums, index):
    if index == len(nums) - 1:
        return nums[index] <= nums[0] and nums[index] <= nums[index - 1]

    else:
        return nums[index] < nums[index + 1] and nums[index] < nums[index - 1]

class Solution:
    def findMin(self, nums: list[int]) -> int:
        begin = 0
        end = len(nums) - 1
        while begin < end:
            mid = (begin + end) // 2
            if check_neighbours(nums, mid):
                return nums[mid]


            if nums[mid] >= nums[end] and nums[begin] > nums[end]:
                begin = mid + 1

            elif nums[mid] <= nums[begin] and nums[begin] > nums[end]:

                end = mid

            elif nums[mid] <= nums[end] and nums[begin] <= nums[mid] and nums[begin] < nums[end]:
                end = mid



        return nums[begin] if check_neighbours(nums, begin) else None


print(Solution().findMin([1]))

