# Name: KYLE ENAD
# Assessment 3.6: DFS Methods in Tree - Post-order


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


def postorder(root):
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        result.append(node.value)   # Root-Right-Left order ...
        stack.append(node.left)
        stack.append(node.right)
    result.reverse()                # ... reversed gives Left-Right-Root
    return result


if __name__ == "__main__":
    tree = build_tree()
    print("Name: KYLE ENAD")
    print("Post-order:", " - ".join(postorder(tree)))