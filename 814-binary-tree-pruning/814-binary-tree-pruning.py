# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        root.left, root.right = map(self.pruneTree, (root.left, root.right))
        if not any((root.left, root.right, root.val)):
            return None
        return root
    
    
#         def prune(node):
# 			if not node:
# 				return False

# 			left = prune(node.left)
# 			if not left:
# 				node.left = None

# 			right = prune(node.right)
# 			if not right:
# 				node.right = None

# 			containsOne = left or right or node.val

# 			if not containsOne:
# 				node.val = None

# 			return containsOne

# 		prune(root)
# 		if root.val is not None:
# 			return root




        # if root:
        #     if root.left: root.left = self.pruneTree(root.left)
        #     if root.right: root.right = self.pruneTree(root.right)
        #     if root.left == None and root.right == None and root.val == 0: return None
        # return root
        
        
        # if not root:
        #     return None
        # root.left=self.pruneTree(root.left)
        # root.right=self.pruneTree(root.right)
        # if root.val==0 and not root.left and not root.right:
        #     return None
        # return root
        