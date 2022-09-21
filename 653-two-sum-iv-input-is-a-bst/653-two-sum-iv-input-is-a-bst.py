# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
#         if not root:
#             return False
        
#         if root.val + self.findTarget(root.left,k) == k or root.val + self.findTarget(root.right,k) == k:
#             return True
#         return False
        
    
    
    
    
#         val = set()
        
#         def finder(node):
#             if not node:
#                 return False
#             if (k-node.val in val):
#                 return True
#             aval.add(node.val)
            
#             return self.subFinder(node.left) or self.subFinder(node.right)
        
#         return self.findTarget(root,k)
    
    
    
    
        a=set()
        def h(node):
            if not node:
                return False
            if(k-node.val in a):
                return True
            a.add(node.val)
            return h(node.right) or h(node.left)
        return h(root)
                
        
        