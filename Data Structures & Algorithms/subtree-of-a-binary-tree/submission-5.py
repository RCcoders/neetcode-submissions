# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isIdentical(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return (
            root1.val == root2.val and
            self.isIdentical(root1.left, root2.left) and
            self.isIdentical(root1.right, root2.right)
        )

    # Main function to check if subRoot is a subtree of root
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True  # An empty tree is always a subtree
        if not root:
            return False  # Non-empty subRoot can't be in an empty tree
        
        # Check if current root matches subRoot OR search in left/right subtrees
        if self.isIdentical(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)