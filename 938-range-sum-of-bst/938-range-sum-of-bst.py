# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        res = []
        def inorder(root):
            if not root:
                return None
            
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        
        inorder(root)
        sum = 0
        for i in res:
            if i >= low and i <= high:
                sum += i
                # print(i,sum)
        return sum
        