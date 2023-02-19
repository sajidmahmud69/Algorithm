# Time Complexity: O(n)
# Space Complexity: O(n)

# result will be the array where we store the answer
# iterate the array from right to left
# at every iteration add the carry with digits[i]
# if the value >= 10 push 0 into beginning of resulting array
# and set carry to 1
# else set carry to 0 and push digits[i] to beginning of
# resulting array 
# at the end of the loop if carry is 1
# push 1 into resulting array

def plusOne (digits):
    result = []
    carry = 1
    
    i = len(digits) - 1
    
    while i > -1:
        if digits[i] + carry == 10:
            result.insert (0, 0)
            carry = 1
        else:
            result.insert (0, digits[i] + carry)
            carry = 0

        i -= 1

    if carry == 1:
        result.insert (0, 1)

    return result




if __name__ == '__main__':
    digits = [9, 8, 9]
    print (plusOne (digits))
