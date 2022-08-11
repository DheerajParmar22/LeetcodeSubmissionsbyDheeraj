# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node, l, h):
            if not node:
                return True
            if not (l < node.val < h):
                return False
            return helper(node.left, l, node.val) and helper(node.right, node.val, h)
        
        return helper(root, -inf, inf)
        
        
        
#         def helper(node,l,r):
#             if not node:
#                 return True
#             if not (l<node.val<r):
#                 return False
            
#             return helper(node.left,l,node.val) and helper(node.right,node.val,r)
        
#         return helper(root,left,right)
        
        
        
        
        
#         if root == None:
#             return True
        
#         if left != None and root.data <= left.data:
#             return False
        
#         elif right != None and root.data >= right.data:
#             return False
        
#         return isValidBST(root.left,left,root) and isValidBST(root.right,root,right)
        
        
        