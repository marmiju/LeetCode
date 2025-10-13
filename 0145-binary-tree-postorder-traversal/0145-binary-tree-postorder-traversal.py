# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    
    def postOrder(self,root):
        if root is None:
            return 
        self.postOrder(root.left)
        self.postOrder(root.right)
        self.ans.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.postOrder(root)
        return self.ans
        