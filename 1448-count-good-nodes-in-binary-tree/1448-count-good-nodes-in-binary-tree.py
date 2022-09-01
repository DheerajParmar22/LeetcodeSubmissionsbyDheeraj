# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node,maxVal):
            if not node:
                return 0
            
            if node.val >= maxVal:
                count = 1
            else:
                count = 0
            
            maxVal = max(maxVal,node.val)
            # return add + dfs(node.left,maxval) + dfs(node.right,maxval)
            count = count + dfs(node.left,maxVal)
            count = count + dfs(node.right,maxVal)
            # return count
        
            return count
        
        return dfs(root, root.val)
                
        