# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. Both nodes are None -> identical at this position
        if not p and not q:
            return True
        
        # 2. One is None while the other isn't -> structural mismatch
        if not p or not q:
            return False
        
        # 3. Values don't match -> value mismatch
        if p.val != q.val:
            return False
        
        # 4. Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        