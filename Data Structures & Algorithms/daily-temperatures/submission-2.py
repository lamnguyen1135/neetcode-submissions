class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        cacheIndex = []
        ans = []
        q = collections.deque()
        for i in range(len(temperatures) - 1, -1, -1):
            while cacheIndex and temperatures[i] >= temperatures[cacheIndex[-1]]:
                cacheIndex.pop()
            
            if not cacheIndex:
                ans.append(0)
                cacheIndex.append(i)
                continue

            ans.append(cacheIndex[-1] - i)
            cacheIndex.append(i)
            
        return ans[::-1]