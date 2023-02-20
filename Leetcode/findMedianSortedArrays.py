class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        totalLength = len(nums1) + len(nums2)
        halfLength = totalLength // 2

        A = nums1
        B = nums2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            # i used for determining small array left side such that A[:i]
            i = (r + l) // 2     # A

            # j used for determining left side of B such that B[:j]
            # remaining elements needed from array B to create left side
            j = halfLength - i - 2      # B[:j]

            a_left = A[i] if i >= 0 else float('-infinity')            # indicates highest value in left side after partioning
            a_right = A[i+1] if (i+1) < len(A) else float('infinity')   # indicates smallest value in right side after partioning
            b_left = B[j] if j >= 0 else float('-infinity')             # indicates highest value in left side after partioning
            b_right = B[j+1] if (j+1) < len(B) else float('infinity')   # indicates smallest value in right side after partioning

            # partition is correct
            if a_left <= b_right and b_left <= a_right:
                # odd
                if totalLength % 2:
                    return min(a_right, b_right)
                
                # even
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
            
            elif a_left > b_right:
                r = i - 1

            else:
                l = i + 1 

