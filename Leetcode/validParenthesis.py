# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# use stack to keep track recent open parenthesis
# use hashMap to keep track of close parenthesis and see if
# the family of parenthesis matches



def isValid (s):

    stack = []
    hashMap = {')':'(', ']':'[', '}':'{'}

    for c in s:
        if c in hashMap:
            if stack and stack[-1] == hashMap[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append (c)

    return True if not stack else False



# Driver Code
print (isValid ('(){}[()]'))
print (isValid ('(]'))
print (isValid ('({[]})'))
print (isValid ('(){[]})'))
