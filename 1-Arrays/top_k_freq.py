def topKFrequent(nums, k):
    uniq = list(set(nums))
    memo = {}
    for i in range(len(uniq)):
        memo[uniq[i]] = 0

    for i in range(len(nums)):
        memo[nums[i]] += 1

    memo_sorted = sorted(memo.items(), key=lambda x: x[1], reverse=True)

    res = []
    for i in range(k):
        res.append(memo_sorted[i][0])

    return res


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))
