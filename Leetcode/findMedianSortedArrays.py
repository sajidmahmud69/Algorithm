class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged_list = []
        merged_list.append(nums1)
        merged_list.append(nums2)

        merged_list.sort()

        # even case
        if len(merged_list) % 2 == 0:
            mid = len(merged_list) // 2
            left = mid - 1 
            right = mid
            ans =  (merged_list[left] + merged_list[right]) / 2
            return ans
        # odd case
        else:
            mid =  len(merged_list) // 2
            ans = merged_list[mid]
            return ans
        
s = Solution()
nums1 = [1, 3]
nums2 = [2]
ans = s.findMedianSortedArrays(nums1, nums2)
print(ans)
