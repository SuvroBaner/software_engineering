class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
#---- Iterative Solution ----
# Avg Time : O(logn) | Space : O(1)
# Worst Time : O(n) | Space : O(n)
def findClosestValueInBst(tree, target):
    closest = float("inf")
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if currentNode.value < target:
            currentNode = currentNode.right
        elif currentNode.value > target:
            currentNode = currentNode.left
        else:
            break
    return closest

#---- Recurssive Solution ----
# Avg Time : O(logn) | Space : O(n)
# Worst Time : O(n) | Space : O(n)
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if tree.value < target:
        return findClosestValueInBstHelper(tree.right, target, closest)
    elif tree.value > target:
        return findClosestValueInBstHelper(tree.left, target, closest)
    else:
        return closest