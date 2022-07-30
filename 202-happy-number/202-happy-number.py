class Solution:
    def isHappy(self, n: int) -> bool:
        
        if n == 1:
            return True
        
        # s = set()
        while n>5:
            n = sum(int(i)**2 for i in str(n))
        return True if n==1 else False
            
        