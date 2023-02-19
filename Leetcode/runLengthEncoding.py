def runLengthEncoding (s):
    if len (s) <= 1:
        return s[0] + "1"
    res = ""
    count = 1

    for i in range (len (s)):
        currChar = s[i]

        if (i < len (s) - 1 and s[i] == s[i+1]):
            count += 1
        else:
            res += currChar + str (count)
            count = 1

    return res


# driver code

if __name__ == '__main__':
    s = "aabbbcaad"
    print (runLengthEncoding(s)) 


# Space and Time Complexity
# Space Complexity: O(1)
# Time Complexity: O(n)
