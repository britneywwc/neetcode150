import math


def productExceptSelf(nums):
    n = len(nums)
    product = [0] * n

    # First and last element starts with 1
    product[0] = 1
    suffixProduct = 1

    for i in range(1, n):
        # Multiply all left product with current left num
        # Only use product[i-1] because all the product is multiplied as we traverse through left to right
        product[i] = product[i-1] * nums[i-1]

    # Traverse backwards, starting from second last element
    for j in range(n-2, -1, -1):
        # Multiply current with accumulated suffixProduct and current right next
        product[j] *= suffixProduct * nums[j+1]

        # Update suffix product
        suffixProduct *= nums[j+1]

    return product


a = [1, 2, 3, 4]
b = [-1, 1, 0, -3, 3]
print(productExceptSelf(b))
