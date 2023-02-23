class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0 and len(t) != 0:
            return True

        stack = []

        for c in s:
            stack.append(c)

        for c in t:
            if len(stack) < 1:
                return True
            if stack[0] == c:
                stack.pop(0)
        return True if len(stack) == 0 else False
    
    def isSubsequence2(self, s, t):
        n = len(s)
        m = len(t)
        j = 0

        i = 0
        j = 0

        while i < m and j < n:
            if s[j] == t[i]:
                j += 1
            i += 1
        return j == n

s = 'a'
t = 'ahbgdc'

obj = Solution()
print(obj.isSubsequence2(s, t))