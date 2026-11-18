class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if nums == []:
            return 0
        nums = set(nums)
        cache = {}

        for num in nums:
            if num-1 not in nums:
                cache[num] = 1
        print(cache)

        
        for key, value in cache.items():
            i = 1
            while key + i in nums:
                cache[key] += 1
                i += 1
        
        return max(cache.values())