class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for x in range(len(nums)):
            if target - nums[x] != nums[x]:
                hashmap[nums[x]] = [target - nums[x], x]
            if target - nums[x] == nums[x] and nums.count(nums[x]) > 1:
                return [x, nums.index(nums[x], nums.index(nums[x]) + 1)]

        for j in range(len(nums)):
            if target - nums[j] in hashmap and nums[j] == hashmap[target - nums[j]][0]:
                return [j, hashmap[target - nums[j]][1]]