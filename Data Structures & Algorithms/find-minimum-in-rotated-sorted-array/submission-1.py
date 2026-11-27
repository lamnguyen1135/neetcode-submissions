class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        ans = float("inf")
        while l <= r:
            middle = int((r+l)/2)
            ans = min(ans, nums[middle])
            print(middle)
            if nums[middle] <= nums[r]: #if middle and r segment are sorted
                r = middle - 1
                
            elif nums[middle] >= nums[r]: #if middle and r segment are not sorted
                l = middle + 1
            #print("left: " + str(l) + " right: " + str(r))
        return ans