# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def travers(root):
            if root:
                travers(root.left)
                travers(root.right)
                ans.append(root.val)
        travers(root)
        return ans
        