class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        #windowLen - mostFreq
        l = 0
        longest = 0
        cache = {}
        for r in range(len(s)):
            cache[s[r]] = cache.get(s[r], 0) + 1
            mostFreq = max(cache.values(), default = 0)
            # print("left: " + str(l) + "right: " + str(r))
            # print(mostFreq)
            while ((r - l + 1 - mostFreq) > k):
                cache[s[l]] -= 1
                l += 1

            
            
            longest = max(r - l + 1, longest)
            
            
        return longest
