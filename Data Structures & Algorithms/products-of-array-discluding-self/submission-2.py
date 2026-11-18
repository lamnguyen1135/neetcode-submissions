class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #starting left

        leftArr = [1]
        
        for i in range(1, len(nums)):
            leftArr.append(leftArr[i-1] * nums[i-1])

        currentNum = 1
        for j in range(len(nums)-2, -1, -1):
            numberTemp = nums[j+1] * currentNum
            currentNum = numberTemp
            leftArr[j] = leftArr[j] * numberTemp
        

        return leftArr
            
                
