class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        biggest = max(piles)
        l = 1
        r = biggest
        ans = biggest
        while l <= r:
            middle = int((l+r)/2)
            total = 0
            for i in range(len(piles)):
                total += math.ceil(piles[i] / middle)
            
            if total <= h:
                ans = min(ans, middle)
                r = middle - 1
            else:
                l = middle + 1
        return ans




