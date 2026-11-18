class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cache = {}

        for i in range(len(s)):
            if s[i] not in cache:
                cache[s[i]] = 1
            else:
                cache[s[i]] += 1

        for j in range(len(t)):
            if t[j] not in cache:
                cache[t[j]] = 1
            else:
                cache[t[j]] -= 1
        for key, value in cache.items():
            if value != 0:
                return False
        return True
        

        

        

