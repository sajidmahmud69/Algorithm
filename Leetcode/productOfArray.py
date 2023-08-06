def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n

    # Calculate the prefix product
    for i in range(1, n):
        result[i] = result[i - 1] * nums[i - 1]

    # Calculate the suffix product and update the result
    suffix_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix_product
        suffix_product *= nums[i]

    return result

if __name__ == '__main__':
    nums1 = [1, 2, 3, 4]
    nums2 = [4,3,2,1,2]
    print(productExceptSelf(nums2))