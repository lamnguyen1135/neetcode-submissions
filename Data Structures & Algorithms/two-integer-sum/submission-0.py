from collections import defaultdict 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        table = defaultdict(int)
        ans = []
        for i in range(len(nums)):
            j = target - nums[i]
            if j in table:
                return [table[j], i]
            table[nums[i]] = i