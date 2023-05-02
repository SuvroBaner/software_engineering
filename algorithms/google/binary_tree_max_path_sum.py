from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self, root: Optional[TreeNode]) -> int:
        result = [root.val]

        # This should return the value for a root node without splitting further down
        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # value at root with splitting
            new_root_val = root.val + leftMax + rightMax
            # update the result 
            result[0] = max(result[0], new_root_val)

            return root.val + max(leftMax, rightMax)
        
        dfs(root)

        return result[0]