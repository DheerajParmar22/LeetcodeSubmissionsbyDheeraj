# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
#         if not root:
#             return []
        
#     def height(Node):
#         if not Node:
#             return 0
#         else:
#             lheight = self.height(node.left)
#             rheight = self.height(node.right)
            
#             if lheight > rheight:
#                 lheight += 1
#             else:
#                 rheight += 1
                
#     def CurrentLevel(root, level):
#         if not root:
#             return None
        
#         if level == 1:
#             return root.val
#         elif level > 1:
#             self.CurrentLevel(root.left,level-1)
#             self.CurrentLevel(root.right,level-1)
        
#         h =  height(root)
#         for i in range(1,h+1):
#             self.CurrentLevel(root, i)
        
    
    
        if not root: return []

        ans = []
        level = [root]

        while level:

            ans.append([node.val for node in level])
            level = [kid for node in level for kid in (node.left, node.right) if kid]

        return ans
    
            
        