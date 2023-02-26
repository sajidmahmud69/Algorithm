class Solution:
    def firstBadVersion(self, n):
        low = 1
        high = n

        while low <= high:
            mid = low + (high - low) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                high = mid - 1
            else:
                low = mid + 1
        return low