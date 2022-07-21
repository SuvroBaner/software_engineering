class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))

# Time : O(n) | Space : O(d) where d is the longest branch in the tree
def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    
    if tree.value < minValue or tree.value >= maxValue:
        return False

    isValidLeft = validateBstHelper(tree.left, minValue, tree.value)
    isValidRight = validateBstHelper(tree.right, tree.value, maxValue)
    return isValidLeft and isValidRight
