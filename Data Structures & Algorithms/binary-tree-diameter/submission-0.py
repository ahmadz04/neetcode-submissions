# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def height(root):
            nonlocal max_diameter
            if not root:
                return 0

            
            height_left = height(root.left)
            height_right = height(root.right)

            curr_diameter = height_left + height_right
            max_diameter = max(max_diameter, curr_diameter)

            return 1 + max(height_left, height_right)
        
        height(root)
        return max_diameter