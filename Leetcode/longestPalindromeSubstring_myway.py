def longestPalindrome(s):
    if len(s) <= 0:
        return 0
    s_len = len(s)
    maxPalindrome = ''
    for i in range(len(s)):
        l, r = i, i

        # odd case
        while l >= 0 and r < s_len and s[l] == s[r]:
            if r - l + 1 > len(maxPalindrome):
                maxPalindrome = s[l : r+1]
            r += 1
            l -= 1
        # even case
        l = i
        r = i + 1
        while l >= 0 and r < s_len and s[l] == s[r]:
            if r - l + 1 > len(maxPalindrome):
                maxPalindrome = s[l : r+1]
            r += 1
            l -= 1
    return maxPalindrome 


if __name__ == '__main__':
    s = 'abba'
    print(longestPalindrome(s))
    s = 'aaaaaaaaababababababababab'
    print(longestPalindrome(s))
