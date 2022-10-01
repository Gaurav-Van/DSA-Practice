# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if root:
            level = [root]
            while level:
                ans.append([i.val for i in level])
                level = [prop for node in level for prop in (node.left, node.right) if prop]
        return ans