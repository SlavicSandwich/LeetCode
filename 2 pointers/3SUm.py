class Solution:
    def threeSum(self, nums: list[int]):
        nums.sort()
        results = list()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            i1 = i + 1
            i2 = len(nums) - 1
            while i1 < i2:
                if nums[i] + nums[i1] + nums[i2] > 0:
                    i2 -= 1

                elif nums[i] + nums[i1] + nums[i2] < 0:
                    i1 += 1

                elif nums[i] + nums[i1] + nums[i2] == 0:
                    results.append([nums[i], nums[i1], nums[i2]])

                    i1 += 1
                    while i1 < len(nums) and nums[i1] == nums[i1 - 1]:
                        i1 += 1



        return results





print(Solution().threeSum([0, 0, 0]))

