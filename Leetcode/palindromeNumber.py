# Given an integer x, return true if x is palindrome integer.
# answer = 0
# 121
# 121 mod 10 = 1
# answer * 10 + 1 => 1
# 121//10 => 12

# answer = 1
# 12 mod 10 => 2
# answer * 10 + 2 => 12
# 12 // 10 => 1
# answer = 12

# 1 mod 10 => 1
# answer * 10 + 1 => 121
# answer = 121
 
def isPalindrome(x):
    target = x
    reversedInteger = 0
    if x < 0:
        return False

    while x >= 10:
        reversedInteger = (reversedInteger * 10) + (x % 10)
        x = x // 10

    reversedInteger = (reversedInteger * 10) + x
    return reversedInteger == target


# Test Code
print (isPalindrome (121))
print (isPalindrome (-121))
print (isPalindrome (1))
print (isPalindrome (10))


# Space Complexity: O(1)
# Time Complexity: O(n)


