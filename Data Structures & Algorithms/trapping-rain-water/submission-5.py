class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftMax = 0
        rightMax = 0
        left, right = 0, len(height) - 1

        ans = 0

        while left < right:
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                ans += leftMax - height[left]
                left += 1
            elif height[right] <= height[left]:
                rightMax = max(rightMax, height[right])
                ans += rightMax - height[right]
                right -= 1
        return ans