class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        cache = set()
        left = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in cache:
                cache.remove(s[left])
                left += 1
            cache.add(s[r])
            longest = max(longest, r - left + 1)

        return longest

        

            

        

