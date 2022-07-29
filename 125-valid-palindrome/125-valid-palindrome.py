class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if s is None:
            return True
        
        ans = ''
        
        for i in s:
            if i.isalnum():
                ans += i.lower()
        return ans==ans[::-1]
        