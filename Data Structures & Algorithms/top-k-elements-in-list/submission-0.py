class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        cache = {}
        for num in nums:
            cache[num] = cache.get(num, 0) + 1

        
        sorted_cache = dict(sorted(cache.items(), key=lambda x: x[1], reverse=True))
        i = 0
        ans = []
        for key, value in sorted_cache.items():
            if i < k:
                ans.append(key)
            else:
                break
            i += 1

        return ans