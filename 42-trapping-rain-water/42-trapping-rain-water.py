class Solution:
    def trap(self, height: List[int]) -> int:
        def trap(self, height: List[int]) -> int:
            if not height:
                return 0
        
        res = 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        
        while l < r:
            if leftMax <= rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
				 #it adds zero if leftMax < height[i] or else it adds leftMax[i] - height[i]
                res += leftMax - height[l]  
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
				 #it adds zero if rightMax < height[i] or else it adds rightMax[i] - height[i]
                res += rightMax - height[r]
                
        return res