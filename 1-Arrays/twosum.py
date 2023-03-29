def twoSum(nums, target):

        n = len(nums)

        for i in range(n):
            curr = nums[i]
            res = [i]

            for j in range(i+1, n):
                curr += nums[j]
                if curr == target:
                    res.append(j)
                    return res
                else:
                    curr -= nums[j]
                    continue

            if curr == target:
                return res


nums = [-3,4,3,90]

target = 0

rest = twoSum(nums, target)