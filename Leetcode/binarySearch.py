class Solution:
    def binarySearch(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                high = mid - 1
        return -1
    
nums = [-1,0,3,5,9,12]
target = 9
s = Solution()
print(s.binarySearch(nums, target))
