# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining


# Time complexity
# O(1) space
# O(n) time

def trap (height):
    # height is an array of integers

    L = 0                               # left pointer
    R = len (height) - 1                # right pointer

    maxLeft = height[L]                 # max left of current pos
    maxRight = height [R]               # max right of current pos

    ans = 0

    while L <= R:
        if maxLeft < maxRight:
            ans += maxLeft - height[L] if (maxLeft - height[L] > 0) else 0
            maxLeft = max (maxLeft, height[L])
            L += 1

        else:
            ans += maxRight - height [R] if (maxRight - height[R] > 0) else 0
            maxRight = max (maxRight, height[R])
            R -= 1

    return ans


# Driver code
if __name__  == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print (trap (height))


