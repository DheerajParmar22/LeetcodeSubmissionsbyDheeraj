class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_sum=-inf
        best_sum=-inf
        
        for i in nums:
            curr_sum = max(i,curr_sum+i)
            best_sum = max(best_sum, curr_sum)
            
        return best_sum
        
        