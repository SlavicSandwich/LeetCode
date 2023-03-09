class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        possible = []
        def iterate(nums:list,possible:list,res, i:int):
            if i == len(nums):
                res.append(possible.copy())
                return

            possible_rec = possible.copy()
            iterate(nums, possible_rec, res, i + 1)
            possible_rec.append(nums[i])
            iterate(nums, possible_rec, res, i + 1)

        iterate(nums, possible, res, 0)
        return res

print(Solution().subsets([1,2,2, 3,3]))


