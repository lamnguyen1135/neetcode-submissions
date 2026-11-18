from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        if len(t) > n:
            return ""
        l, r = 0, 0
        length = float("inf")
        ans = (0,0)
        window = defaultdict(int)
        countT = defaultdict(int)
        have = 0
       
        for i in range(len(t)):
            countT[t[i]] += 1
        need = len(countT)
        while r < n:
            c = s[r]
            window[c] += 1
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                v = s[l]
                window[v] -= 1
                if r-l+1 < length:
                    length = r-l+1
                    ans = l, r
                if v in countT and window[v] < countT[v]:
                    have -= 1
                l += 1

            r += 1
        if length == float("inf"):
            return ""
        left, right = ans
        return s[left: right + 1]
