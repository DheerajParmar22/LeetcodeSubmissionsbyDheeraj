# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def getPaths(root,path,ans):
            if not root:
                return
            # take case - classic backtracking
            path.append(root.val)
            # if current node is a leaf
            if not root.left and not root.right:
                # condition satisfied
                if sum(path) == targetSum:
                    ans.append(path.copy())
                # not take case - classic backtracking
                del path[-1]
                return
            # recurse on kids
            getPaths(root.left,path,ans)
            getPaths(root.right,path,ans)
            # not take case - classic backtracking
            del path[-1]
            
        path = []
        ans = []
        getPaths(root,path,ans)
        return ans