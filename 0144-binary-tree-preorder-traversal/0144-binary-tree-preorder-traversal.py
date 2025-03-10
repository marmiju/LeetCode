# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def travers(root):
            if root:
                ans.append(root.val)
                travers(root.left)
                travers(root.right)
        travers(root)
        return ans

        