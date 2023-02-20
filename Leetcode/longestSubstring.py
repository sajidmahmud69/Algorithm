class Solution:
    # 2 pointer stupid solution
    # def lengthOfLongestSubstring(self, s: str) -> int:
        
        # ans = 0
        # for i in range(len(s)):
        #     tmp = 0
        #     hashMap = {}
        #     for j in range(i, len(s)):
        #         if s[j] not in hashMap:
        #             hashMap[s[j]] = 1
        #             tmp += 1
        #         else:
        #             break
        #     ans = max(ans, tmp)
                
        # return ans

    # sliding window
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res
