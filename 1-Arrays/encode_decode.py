def encode(strs):
    # write your code here
    res = ''
    for i in range(len(strs)):
        res += strs[i]
        if i < len(strs)-1:
            res += ":;"
    return res


def decode(str):
    return str.split(":;")


a = ["we", "say", ":", "yes"]
b = encode(a)
c = decode(b)
print(b, c)
