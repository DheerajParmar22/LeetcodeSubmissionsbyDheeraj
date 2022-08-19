class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        counter = collections.Counter(nums)
        end = defaultdict(int)
        
        for num in nums:
            
            if counter[num] == 0:
                continue
            
            if num-1 in end and end[num-1] > 0:
                end[num-1] -= 1
                end[num] += 1
            elif num+1 in counter and num+2 in counter and counter[num+1] > 0 and counter[num+2] > 0:
                counter[num+1] -= 1
                counter[num+2] -= 1
                end[num+2] += 1
            else:
                return False
            
            counter[num] -= 1
            
        return True
                
            
            