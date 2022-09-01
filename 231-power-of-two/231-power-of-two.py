class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0:
            return False
        
        # while n != 1:
        if n%2 != 0:
            # n = isPowerOfTwo(n/2)
            return False
        else:
            return self.isPowerOfTwo(n/2)
        
        return True
        