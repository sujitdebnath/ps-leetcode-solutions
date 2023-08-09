class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkTree(self, root):
        return root.val == (root.left.val + root.right.val)


root        = TreeNode(10)
left_child  = TreeNode(4)
right_child = TreeNode(6)

root.left  = left_child
root.right = right_child

sol = Solution()
print(sol.checkTree(root))