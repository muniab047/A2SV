# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter=defaultdict(int)
        max_frequency=0
        ans=[]
        def traverse(root):
            nonlocal max_frequency
            if not root:
                return
            counter[root.val]+=1
            max_frequency=max(counter[root.val],max_frequency)

            traverse(root.left)
            traverse(root.right)

        traverse(root)
        for key in counter:
            if counter[key]==max_frequency:
                ans.append(key)

        return ans
        
        