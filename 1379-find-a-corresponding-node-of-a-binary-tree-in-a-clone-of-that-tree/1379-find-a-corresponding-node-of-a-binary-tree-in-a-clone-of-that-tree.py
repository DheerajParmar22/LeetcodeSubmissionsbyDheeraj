# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        # if not original or not cloned:
        #     return
        if cloned is None:
            return cloned
        
        if cloned.val == target.val:
            return cloned
        
        d = self.getTargetCopy(original.left,cloned.left,target)
        if d!= None:
            return d
        parmar = self.getTargetCopy(original.right,cloned.right,target)
        if parmar != None:
            return parmar
        
    
        # return getTargetCopy()
        
        
        
        