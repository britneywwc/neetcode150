import math


def isPalindrome(s: str) -> bool:
    word = ''.join(filter(str.isalnum, s)).lower()
    print(word)
    i = 0
    j = len(word)-1

    while i < math.ceil(len(word)//2):
        if word[i] != word[j]:
            return False

        if i == j:
            break

        i += 1
        j -= 1

    return True


print(isPalindrome("0P"))




