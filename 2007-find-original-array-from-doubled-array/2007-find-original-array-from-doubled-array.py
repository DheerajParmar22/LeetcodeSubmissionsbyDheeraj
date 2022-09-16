class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        if len(changed) == 0 or len(changed) %2 == 1:
            return []
        # for i in range(len(changed)):
        #     if changed[i] == 2*changed[i]:
        #         return changed[i]
        #     # else:
        #     #     return []

        
        count = Counter(changed)
        ans = []
        print(count)
        changed.sort()
        
        for i in changed:
            if i == 0 and count[i]>=2:
                count[i] -= 2
                ans.append(i)
            elif i>0 and count[i] and count[i*2]:
                count[i] -= 1
                count[i*2] -= 1
                ans.append(i)
                
        if len(ans) == len(changed)//2:
            return ans
        else:
            return []