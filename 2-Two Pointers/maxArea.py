def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        if height[left] <= height[right]:
            area = (right-left) * height[left]
            left += 1
        else:
            area = (right-left) * height[right]
            right -= 1

        if area > max_area:
            max_area = area

    return max_area


h = [1,8,6,2,5,4,8,3,7]
print(maxArea(h))
