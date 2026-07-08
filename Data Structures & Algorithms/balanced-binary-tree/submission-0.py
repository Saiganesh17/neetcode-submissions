# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def calculate_height(node: Optional[TreeNode])-> int:
            if node is None:
                return 0
            left_height= calculate_height(node.left)
            right_height= calculate_height(node.right)
            if (left_height == -1 or 
                right_height == -1 or 
                abs(left_height - right_height) > 1):
                return -1  # Return -1 to indicate unbalanced tree
          
            # Return height of current subtree (1 + maximum height of children)
            return 1 + max(left_height, right_height)
        return calculate_height(root)>= 0
        #Time and space complexity is O(n) & O(n) respectively
        #pitfall1: Attempting top down approach with separate height calculation
        #pitfall2: Forgetting to check subtree balance status
        #pitfall3: confusing height with depth or number of nodes
        