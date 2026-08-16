# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If subroot is null, it definitely is the subtree of root
        # If subroot is not null and root is null, return False - Not a subtree
        if not subRoot:
            return True
        if not root and subRoot:
            return False
        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))

        
    def sameTree(self, s, t):
        # Start at both roots: are they the same? If yes, match starts here. If not, check the left subtree and the right subtree
        # If root and subroot are both empty, they are the same tree
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and
            self.sameTree(s.right, t.right))