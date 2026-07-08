# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(tree1:Optional[TreeNode], tree2:Optional[TreeNode])-> bool:
            if tree1 is None or tree2 is None:
                return tree1 is tree2
            return (tree1.val== tree2.val and is_same_tree(tree1.left, tree2.left) and is_same_tree(tree1.right, tree2.right))
        if root is None:
            return False
        return (is_same_tree(root, subRoot) or self.isSubtree(root.left, subRoot)or self.isSubtree(root.right, subRoot))
        #Time complexity is O(n * m)
        #Space complexity is O(n)
        #pitfall1: Confusing subtree with substructure
        #pitfall2: Incorrecr base case handling
        #pitfall3: Missing edge caseL Empty subroot
        #pitfall4: performance degradation with repeated values
        #pitfall5: stack overflow with deep trees 
