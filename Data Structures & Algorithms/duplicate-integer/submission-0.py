class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in nums:
            if i not in count:
                count[i] = count.get(i, 0)  + 1
            else:
                count[i] += 1
            print(count[i])
            if count[i] == 2:
                return True
        return False
                

