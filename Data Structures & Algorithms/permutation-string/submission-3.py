class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cache = {}
        for char in s1:
            cache[char] = cache.get(char, 0) + 1
        

        s1Length = len(s1)
        if s1Length > len(s2):
            return False
        
        l = 0
        cacheTwo = {}
        
        for r in range(len(s2)):
            cacheTwo[s2[r]] = cacheTwo.get(s2[r], 0) + 1
            if r > len(s1)-1:
                if cacheTwo[s2[l]] > 1:
                    cacheTwo[s2[l]] -= 1
                else:
                    cacheTwo.pop(s2[l], None)
                l += 1

            if cacheTwo == cache:
                    return True
        return False


            