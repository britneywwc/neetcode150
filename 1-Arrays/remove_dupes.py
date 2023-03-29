def removeDuplicates(nums):
    if not nums:
        return

    i = j = 0
    while j < len(nums):
        if nums[i] != nums[j]:
            nums[i + 1] = nums[j]
            i += 1
        j += 1
    return nums, i + 1


nums = [1, 2, 2]

res = removeDuplicates(nums)
