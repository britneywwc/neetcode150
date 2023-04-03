if len(s1) > len(s2): return False

    s1Count, s2Count = [0] * 26, [0] * 26

    # Loop through s1, get the indices of len(s1)
    # Update s1Count[s1[0]] to 1
    # > s1Count["a"] = 1    |   s1Count["b"] = 1    |   s1Count["c"] = 1
    # Updates s2Count first 3 characters
    # > s2Count["e"] = 1    |   s2Count["e"] = 1    |   s2Count["d"] = 1
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s1[i]) - ord('a')] += 1

    # Loop through both counts and update matches
    matches = 0
    for i in range(26):
        if s1Count[i] == s2Count[i]:
            matches += 1

    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26: return True

        # Pointer at new s2 char, update count
        index = ord(s2[r]) - ord('a')
        s2Count[index] += 1

        # Check if current s2 char matches with s1 count, increase matches
        if s1Count[index] == s2Count[index]:
            matches += 1
        
        # Check if previously matched, new index is moving away from a match so -=1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1
        
        
        index = ord(s2[l]) - ord('a')
        s2Count[index] -= 1

        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1
        l += 1

    return matches == 26