class Solution:

    # # brute force
    # # Time Complexity: O(n^3)
    # # Space Complexity: O(1)
    
    # def longestPalindrome(self, s):
    #     if len(s) == 0 or len(s) == 1:
    #         return s
        
    #     longestPalindrome = ''
    #     for i in range(len(s)):
    #         for j in range(i, len(s)):
    #             word = s[i:j+1]
    #             is_palindrome = self.isPalindrome(word)

    #             if is_palindrome:
    #                 if len(word) > len(longestPalindrome):
    #                     longestPalindrome = word

    #     return longestPalindrome
    
    
    
    def isPalindrome(self, s):
        if len(s) == 0 or len(s) == 1:
            return True
        
        l_ptr = 0
        r_ptr = len(s) - 1

        while l_ptr <= r_ptr:
            if s[l_ptr] != s[r_ptr]:
                return False
            l_ptr += 1
            r_ptr -= 1
            
        return True


    # slightly optimized
    def longestPalindrome(self, s):
        hashMap = {}
        res = ''
        for i in range(len(s)):
            for j in range(len(s)):
                word = s[i:j+1]
                
                if word in hashMap:
                    continue

                else:
                    hashMap[word] = self.isPalindrome(word)
        
        for k, v in hashMap.items():
            if v and len(k) > len(res):
                res = k

        return res




s = Solution()
word = "abcd"
ans = s.longestPalindrome(word)
print(ans)