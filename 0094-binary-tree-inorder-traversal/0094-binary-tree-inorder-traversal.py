# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    
    def inOrder(self,root):
        if root is None:
            return 
        self.inOrder(root.left)
        self.ans.append(root.val)
        self.inOrder(root.right)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.inOrder(root)
        return self.ans
        