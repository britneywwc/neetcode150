def minWindow(s, t):
    if t == "":
        return ""
    
    # Preprocess t into hash map
    count = {}
    for i in t:
        count[i] = 1
    
    print(count)
    
    # Start comparing
    smallest = (-1, -1)
    index = (-1, -1)
    l = 0

    while l < len(s) - len(t):
        break

    return
    

s = "ADOBECODEBANC"
t = "ABCB"
print(minWindow(s, t))
