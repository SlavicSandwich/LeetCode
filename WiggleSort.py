def wiggleSort(nums):
    peak = False
    for i in range(len(nums) - 1):
        if peak:
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

            peak = False
        else:
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

            peak = True




    return nums


print(wiggleSort([3,5,2,1,6,4]))

nums =  [3,5,1,6,2,4]

