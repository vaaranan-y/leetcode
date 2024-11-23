# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    
        def getLeafSequence(node):
            if(node == None):
                return []
            elif(node.left == None and node.right == None):
                return [node.val]
            else:
                leftSeq = getLeafSequence(node.left)
                rightSeq = getLeafSequence(node.right)
                res = leftSeq + rightSeq
                return res
        
        seq1 = getLeafSequence(root1)
        seq2 = getLeafSequence(root2)
        
        print(seq1)
        print(seq2)
        

        return seq1 == seq2

        