class Solution:

    def isReflective(self, L: Optional[TreeNode], R: Optional[TreeNode]) -> bool:
        if(not L and not R):
            return True
        elif(not L or not R):
            return False
        else:
            return L.val == R.val and self.isReflective(L.left, R.right) and self.isReflective(L.right, R.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isReflective(root.left, root.right)