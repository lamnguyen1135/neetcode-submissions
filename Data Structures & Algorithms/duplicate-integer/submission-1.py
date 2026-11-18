class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        cache = {}
        for n in nums:
            if n not in cache:
                cache[n] = 1
            else:
                cache[n] += 1

            if cache[n] > 1:
                return True
        return False