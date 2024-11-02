# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if(not root):
            return []
        else:
            leftSide = self.postorderTraversal(root.left)
            rightSide = self.postorderTraversal(root.right)
            res = leftSide + rightSide
            res.append(root.val)
            return res
        