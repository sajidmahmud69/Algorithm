def rob(nums):
    if len(nums) <= 2:
        return max(nums)
    
    prevOne = nums[1]
    prevTwo = nums[0]

    for i in range(2, len(nums)):
        maxRob = max (prevTwo + nums[i], prevOne)
        prevTwo = max(prevOne, prevTwo)
        prevOne = maxRob

    return prevOne 


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(rob(nums))
    nums = [2, 7, 9, 3,1]
    print(rob(nums))
    nums = [2, 1, 1, 2]
    print(rob(nums))
