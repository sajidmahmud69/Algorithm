# Given an array of integers and a target integer return indices of the 
# two numbers that add up to target

def twoSum (nums, target):
    hashMap = {}
    for i in range (len (nums)):
        remainder = target - nums[i]
        if remainder in hashMap:
            return [i, hashMap[remainder]]
        hashMap[nums[i]] = i

    return []


# Test cases
print (twoSum ([2, 7, 11, 15], 9))
print (twoSum ([3, 2, 4], 6))
print (twoSum ([3, 3], 6))


# Space Complexity: O(n)
# Time Complexity: O(n)
