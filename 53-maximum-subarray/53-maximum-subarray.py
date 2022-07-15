class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Solution1 - time_complexity is 1194ms
        curr_sum=-inf
        best_sum=-inf
        
        for i in nums:
            curr_sum = max(i,curr_sum+i)
            best_sum = max(best_sum, curr_sum)
            
        return best_sum
    
    
    
    
    

        # Solution2 - time_complexity is 989ms
        max_seen = max_seen_so_far = nums[0]
        
        for i in range(1,len(nums)):
            if max_seen > 0:
                max_seen += nums[i]
            else:
                max_seen = nums[i]
            
            if max_seen > max_seen_so_far:
                max_seen_so_far = max_seen
                
        return max_seen_so_far