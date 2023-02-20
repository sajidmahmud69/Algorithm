class Solution:
    def pivotIndex(self, nums):
        leftSum = 0
        rightSum = sum(nums)

        for i in range(len(nums)):
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1
    

if __name__ == '__main__':

    nums = [2, 1, -1]
    s = Solution()
    print(s.pivotIndex(nums))

