# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If we're checking an empty tree to be a subtree of a root, it's always true
        # If Root is empty, subroot is non empty, return False
        if not subRoot: 
            return True
        if not root and subRoot: return False
        if self.sameTree(root, subRoot):
            return True

        # If they are not the same, we can compare subrtree with the left subtree of root and right subtree of root
        return(self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))

        # Base Case:

    def sameTree(self, s, t):
        # If S is empty and T is empty, they are the same tree
        if not s and not t:
            return True
        # If S and T are both non empty and both their values are the same
        if s and t and s.val == t.val:
            # Still have to compare the left and right subtrees
            # If both of these return true, return that value
            return (self.sameTree(s.left, t.left) and
            self.sameTree(s.right, t.right))

        # If they're not empty compare them
        # If both S and T are not empty



        # If both trees are empty, return true
        # If both trees are not empty, comapre the two
        # If at least one of the trees is empty and other is not, return False

        