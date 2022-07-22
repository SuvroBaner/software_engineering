class balancedBrackets:
    def __init__(self, string):
        self.string = string

    # Time : O(n) | Space : O(n)
    def solution1(self):
        open_close_br_map = {'(': ')', '[': ']', '{': '}'}
        valid_elements = ['(', ')', '{', '}', '[', ']']
        balanced_stack = []
        for item in self.string:
            if item not in valid_elements:
                continue
            if item in open_close_br_map:
                balanced_stack.append(item)
            else:
                if len(balanced_stack) == 0:
                    return False
                ele = balanced_stack.pop()
                if open_close_br_map[ele] != item:
                    return False
        return True if len(balanced_stack) == 0 else False

# ----- Testing the solution ---
string = "([])(){}(())()()"
string = "123"
string = "}}}"
string = "((("
string = "(a)"
obj = balancedBrackets(string)
print(obj.solution1())