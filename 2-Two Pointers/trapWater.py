def trap(height):
    if len(height) == 0:
        return 0

    l, r = 0, len(height) - 1
    maxL, maxR = height[l], height[r]
    water = 0

    while l < r:
        if maxL < maxR:
            l += 1
            maxL = max(maxL, height[l])
            water += maxL - height[l]
        else:
            r -= 1
            maxR = max(maxR, height[r])
            water += maxR - height[r]

    return water


h = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# h = [4,2,0,3,2,5]
print(trap(height=h))
