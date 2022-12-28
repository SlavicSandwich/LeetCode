def binsearch(nums: list[int], target: int) -> int:
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


def modBinSearch(matrix: list[list[int]], target: int) -> int:
    begin = 0
    end = len(matrix) - 1
    while begin < end:
        mid = (begin + end) // 2
        if target < matrix[mid][0]:
            end = mid

        elif target > matrix[mid][-1]:
            begin = mid + 1

        else:
            return mid

    if matrix[begin][0] <= target <= matrix[begin][-1]:
        return begin

    return -1


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        memo = modBinSearch(matrix, target)
        if memo == -1:
            return False

        return True if binsearch(matrix[memo], target) >= 0 else False


print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 16))
