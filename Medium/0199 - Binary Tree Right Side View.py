# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        
        if root:
            level = [root]
            while level :
                ans.append(level[-1].val)
                level=[prop for node in level for prop in (node.left, node.right) if prop]
        return ans
