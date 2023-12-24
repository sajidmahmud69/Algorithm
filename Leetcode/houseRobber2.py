def rob1(nums):
    if len(nums) <= 2:
        return max(nums)
    
    prevOne = nums[1]
    prevTwo = nums[0]

    for i in range(2, len(nums)):
        maxRob = max (prevTwo + nums[i], prevOne)
        prevTwo = max(prevOne, prevTwo)
        prevOne = maxRob

    return prevOne 

def rob2(nums):
    if len(nums) <= 2:
        return max(nums)
    return max(rob1(nums[:-1]), rob1(nums[1:]))


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(rob2(nums))
    nums = [2, 3, 2]
    print(rob2(nums))
    nums = [1, 2, 3]
    print(rob2(nums))
