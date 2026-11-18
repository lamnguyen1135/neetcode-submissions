class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        cache = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        
        left, right = 0, len(s)-1
        while left < right:
            while left<right and s[left] not in cache:
                left += 1
            while right>left and s[right] not in cache:
                right -= 1
            
            if s[right].lower() != s[left].lower():
                return False
            left += 1
            right -= 1
        
        return True
