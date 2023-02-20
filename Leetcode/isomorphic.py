class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # n = len(s) = len(t)
        # m = unique values in hashMap

        # Method 1
        # Time Complexity: O(n * m) + O(n)
        # Space Complexity: O(m)

        # hashMap = {}
        # for i in range(len(s)):
        #     if t[i] in hashMap.values() and s[i] not in hashMap:
        #         return False

        #     if s[i] not in hashMap:
        #         hashMap[s[i]] = t[i]
        
        # for i in range(len(t)):
        #     if t[i] != hashMap[s[i]]:
        #         return False
        # return True


        # Method 2
        # Time Complexity: O(n) + o(n) => O(n)
        # Space Complexity: O(n) + O(n) => O(n)

        hash1 = []
        hash2 = []
        for c in s:
            hash1.append(s.index(c))
        
        for c in t:
            hash2.append(t.index(c))

        return hash1 == hash2


if __name__ == '__main__':
    s = Solution()
    word1 = 'egg'
    word2 = 'add'
    print(s.isIsomorphic(word1, word2))

    word3 = 'bacon'
    word4 = 'cheez'
    print(s.isIsomorphic(word3, word4))


