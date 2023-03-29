def longestConsecutive(nums) -> int:
    if len(nums) == 0:
        return 0

    nums.sort()
    longest, curr = 1, 1

    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] == 1:
            curr += 1
        elif nums[i] - nums[i-1] == 0:
            pass
        else:

            # reset the curr
            if curr > longest:
                longest = curr

            curr = 1

    if longest < curr:
        return curr
    return longest


a = [1,2,0,1]
print(longestConsecutive(a))
