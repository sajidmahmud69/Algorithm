def maximumConsecutiveOnes(nums, k):
    i, j, zerosFlipped, maxOnes = 0, 0, 0, 0

    while j < len(nums):
        if nums[j] == 0:
            zerosFlipped += 1
        if zerosFlipped <= k:
            maxOnes =  max(maxOnes, len(nums[i:j]) + 1)
        else:
            if nums[i] == 0:
                zerosFlipped -= 1
            i += 1
        j += 1
    return maxOnes


if __name__ == '__main__':
    nums1 = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k1 = 2
    nums2 = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k2 = 3
    print(maximumConsecutiveOnes(nums1, k1))
    print(maximumConsecutiveOnes(nums2, k2))

        