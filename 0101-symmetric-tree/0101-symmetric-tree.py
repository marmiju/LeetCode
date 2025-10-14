# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self,left,right):
        
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False

        if left.val != right.val:
            return False
        
        if not self.isSame(left.left, right.right):
            return False
        
        if not self.isSame(left.right, right.left):
            return False
        
        return True


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return []

        return self.isSame(root.left, root.right)


        