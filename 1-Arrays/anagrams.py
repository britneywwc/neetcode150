def groupAnagrams(strs):
    result = {}     # init dictionary (Key: sorted alphabets, Values: anagram)

    for i in range(len(strs)):
        x = "".join(sorted(strs[i]))        # sort the alphabets of word

        if x in result:
            result[x].append(strs[i])       # anagram exists, append to values
        else:
            result[x] = [strs[i]]           # anagram doesn't exist, create new key-value pair

    return list(result.values())


def isAnagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    n = len(s)

    s_memo = [0] * 27
    t_memo = [0] * 27

    for i in range(n):
        s_index = ord(s[i]) - 96
        t_index = ord(t[i]) - 96

        s_memo[s_index] += 1
        t_memo[t_index] += 1

    for j in range(26):
        if s_memo[j] != t_memo[j]:
            return False

    return True


strss = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strss))


