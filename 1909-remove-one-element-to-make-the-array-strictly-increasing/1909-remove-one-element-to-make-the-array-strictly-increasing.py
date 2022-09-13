class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        
        
#         for i in range (len(nums)):
#             if nums[i-1] < nums[i]:
#                 return True
           
        
#         count = 0
#         for i in range(len(nums)):
#             while count < 1:
#                 if nums[i-1] >= nums[i]:
#                     nums.remove(nums[i])
#                     count += 1
#                     return False
#                 else:
#                     return True
                  
                    
                    
        # count = 0
        # for i in range(len(nums)-1):
        #     new = nums[:i] + nums[i+1:]
        #     for j in range (len(new)):
        #         if new[j-1] <= new[j]:
        #             break
        #         else:
        #             count += 1
        #     if count == len(new)-1:
        #         return True
        #     # count = 0
        # return False
        
        for i in range(len(nums)):
            l = nums.copy()
            l.pop(i)
            if l == sorted(set(l)):
                return True
            else:
                continue
        return False
            