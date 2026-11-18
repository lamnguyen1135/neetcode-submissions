class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        cache = {}
        ans = []
        for i in range(len(nums)):
            number = target - nums[i]
            if cache and nums[i] in cache:
                ans.append(cache[nums[i]])
                ans.append(i)
            cache[number] = i
        print(cache)

        return ans