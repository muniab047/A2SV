# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans=None

        def find(root):
            if not root:
                return
            print(root.val)

            if root.val==val:
                return root
            left=find(root.left)
            if left:
                return left
            return find(root.right)
    

        return find(root)
        


        