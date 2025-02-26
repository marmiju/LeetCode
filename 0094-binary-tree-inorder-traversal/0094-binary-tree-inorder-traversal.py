# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def travers(root):
            nonlocal ans
            if root:
                travers(root.left)
                ans.append(root.val)
                travers(root.right)
        travers(root)
        return ans
            



        