def minWindow(s, t):
    if t == "":
        return ""
    
    # Preprocess t into hash map
    count = {}
    for i in t:
        count[i] = 1
    
    # Start comparing
    smallest = (-1, -1)

    return
    

s = "ADOBECODEBANC"
t = "ABCB"
print(minWindow(s, t))
