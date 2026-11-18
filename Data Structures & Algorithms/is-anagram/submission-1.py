from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table1 = defaultdict(int)
        table2 = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            table1[s[i]] += 1
            table2[t[i]] += 1
        for keys in table1:
            if table1[keys] != table2[keys]:
                return False
        return True
            
        