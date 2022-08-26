class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        num = sorted(str(n))
        for i in range(32):
            current_num = sorted(str(2**i))
            if num == current_num:
                return True
        return False
        
#         if n<0:
#             return False
#         if n == 1:
#             return True
                
#         for i in range(0,n):
#             if pow(2,i) == n:
#                 return list(permutations(i,len(i)))
            
        