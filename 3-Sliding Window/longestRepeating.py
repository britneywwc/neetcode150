def longestRepeating(s, k):
    left, res, maxF = 0, 0, 0
    count = {}

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        maxF = max(maxF, count[s[right]])

        while (right-left+1) - maxF > k:
            count[s[left]] -= 1
            left += 1
        
        res = max(res, right-left+1)

    return res


s = "ABAB"
k = 2
print(longestRepeating(s, k))