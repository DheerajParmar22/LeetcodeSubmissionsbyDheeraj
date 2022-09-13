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
        
        
        
#         Since what we concern about is this condition - "after removing exactly one element, the remaining elements will be strictly increasing or not". Once it meets the above condition, we end our for loop and return True. Otherwise, False is returned.

# The pop(index) will remove the item at the given position in the list and return it. It means if I do it on the original list, it will change the list directly. (i.e., nums.pop(i))
# So I choose to use copy() instead to keep our original list and initialize the copy list every time for following modification and check. (i.e., l = nums.copy())

# For if-else statement, it means after removing exactly one specific position element, if the remaining elements are strictly increasing, we end the for loop and return True. But if not, we use continue to skip the rest of the code in the current iteration of the loop and continue on with the next iteration.

# Back to #1, if each iteration of the for loop is checked and there is no condition that matches what we want, then False is returned.
        for i in range(len(nums)):
            l = nums.copy()
            l.pop(i)
            if l == sorted(set(l)):
                return True
            else:
                continue
        return False
            