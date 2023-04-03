import math
import collections

def maxSlidingWindow(nums, k):
    l = r = 0
    q = collections.deque()
    res = []

    while r < len(nums):
        # Remove queue from left if it is lesser than current
        while q and nums[r] > nums[q[-1]]:
            q.pop()

        # Add to queue
        q.append(r)

        # Check if left is out of bounds
        if l > q[0]:
            q.popleft()
        
        # If window is at least k size, add the current max (leftmost) from queue to output
        if (r + 1) >= k:
            res.append(nums[q[0]])
            l += 1

        r += 1

    return res

a = [1,3,-1,-3,5,3,6,7]
b = 3

a = [7, 2, 4]
b = 2
print(maxSlidingWindow(a, b))
