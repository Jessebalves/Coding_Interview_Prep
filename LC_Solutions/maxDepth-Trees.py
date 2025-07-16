# Maximum Depth for a binary tree problem
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node
# down to the farthest leaf node.
#--------------------------------------------------------->
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left_counter = 0
        right_counter = 0

        if not root:
            return 0 

        if root:
            left_counter += 1
            right_counter += 1
        
        if root.left:
           left_counter += self.maxDepth(root.left)
        if root.right:
            right_counter += self.maxDepth(root.right)
        
        #print("Left: ", left_counter)
        #print("Right:", right_counter)
        if left_counter > right_counter:
            return left_counter
        else:
            return right_counter
