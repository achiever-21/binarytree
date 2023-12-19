#gien a binary tree write all the nodes in inorder (left,root,right)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        stack=[]
        curr=root
        while curr is not None or stack:
            while curr is not None:
                stack.append(curr)  
                curr=curr.left 
            curr=stack.pop()
            res.append(curr.val)
            curr=curr.right 
        return res


        




        
