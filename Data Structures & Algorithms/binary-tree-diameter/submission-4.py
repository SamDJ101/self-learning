# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dia = 0
        def Depth(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            l_depth = Depth(root.left)
            r_depth = Depth(root.right)

            self.max_dia = max(self.max_dia, l_depth+r_depth)
            return 1 + max(l_depth, r_depth)

        Depth(root)
        return self.max_dia
 
        
            
        
        