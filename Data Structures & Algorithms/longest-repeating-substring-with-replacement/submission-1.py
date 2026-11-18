from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        r, l = 0,0
        res = 0
        map = defaultdict(int)
        map[s[0]] += 1
        while r != n:
            #print("left: " + str(l) + ", right: " + str(r))

            if ((r - l) - max(map.values()) + 1 <= k):
                res = max((r - l)+1, res)
                r += 1
                print(r)
                if r == n:
                    return res
                map[s[r]] += 1
            else:
                map[s[l]] -= 1
                l += 1
            

        return res
            









