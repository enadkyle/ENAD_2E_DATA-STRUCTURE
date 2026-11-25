# Name: KYLE ENAD
# Assessment 3.6: DFS Methods in Tree - In-order


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_tree():
    left_branch = Node("Y",
                       Node("E", Node("D")),
                       Node("E"))
    right_branch = Node("L", Node("N"), Node("A"))
    return Node("K", left_branch, right_branch)


def inorder(root):
    result = []
    stack = []
    current = root
    while current is not None or stack:
        while current is not None:      # go as far left as possible
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.value)    # Root
        current = current.right         # then Right
    return result


if __name__ == "__main__":
    tree = build_tree()
    print("Name: KYLE ENAD")
    print("In-order:", " - ".join(inorder(tree)))