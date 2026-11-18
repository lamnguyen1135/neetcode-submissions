class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cache = {}
        

        left = 0
        right = 0  
        res = 0
        
        while right < len(s):
            cache[s[right]] = cache.get(s[right], 0) + 1
            windowLen = right - left + 1
            mostFreq = max(cache.values())
            while windowLen - mostFreq > k:
                cache[s[left]] -= 1
                left += 1
                windowLen = right - left + 1
                mostFreq = max(cache.values())
            res = max(res, windowLen)
            right += 1
                
        return res
            

            


            