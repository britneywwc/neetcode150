def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1

    while l < r:
        curr = numbers[l] + numbers[r]

        if curr > target:
            r -= 1
        elif curr < target:
            l += 1
        else:
            return [l+1, r+1]

a = [5, 25, 75]
target = 100
print(twoSum(a, target))
