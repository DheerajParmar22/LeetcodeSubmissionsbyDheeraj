# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node,sum):
            print(sum)
            if not node:
                return False
            
            sum += node.val
            
            if not node.left and not node.right:
                return sum == targetSum
            
            return (dfs(node.left,sum) or dfs(node.right,sum))
        
        return dfs(root,0)

#         def dfs(node, trSum):
#             if node == None:
#                 return False
#             print(trSum)
#             if node.left == None and node.right == None and trSum == node.val:
#                 return True
            
#             return dfs(node.left, trSum-node.val) or dfs(node.right, trSum-node.val)
        
#         return dfs(root, targetSum)