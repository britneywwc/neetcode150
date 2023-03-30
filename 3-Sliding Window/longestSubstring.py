def lengthOfLongestSubString(s):
    if len(s) == 1:
        return 1
    elif len(s) == 0:
        return 0

    memo = {}
    longest, curr_len, i = 0, 0, 0

    while i < len(s):
        # Non-repeating, add to memo
        if s[i] not in memo:
            memo[s[i]] = i
            curr_len += 1

        # Repeating, reset memo and move pointer next to found
        else:
            if longest < curr_len:
                longest = curr_len

            pointer = memo[s[i]] + 1
            if pointer == len(s):
                break

            # i is currently the next-non repeating index, no need to compare just add to memo
            i = pointer
            memo.clear()
            memo[s[i]] = i
            curr_len = 1

        # Move i to next comparison
        i += 1

    if curr_len > longest:
        return curr_len
    return longest


sample = "abcabcbb"
print("Longest:", lengthOfLongestSubString(sample))
