# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans=0

        def sumNodes(root):
            nonlocal ans
            if not root:
                return

            if root.val>=low and root.val<=high:
                ans+=root.val
                print(root.val)
            sumNodes(root.left)
            sumNodes(root.right)
        sumNodes(root)
        return ans


        