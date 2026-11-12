from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree():
    #        E
    #       / \
    #      N   A
    #     /
    #    D
    root = Node("E")
    root.left = Node("N")
    root.right = Node("A")
    root.left.left = Node("D")
    return root


def bfs(root):
    """Level-order traversal using a queue."""
    result = []
    if root is None:
        return result
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def dfs(root):
    """Pre-order (Root -> Left -> Right) traversal using a stack."""
    result = []
    if root is None:
        return result
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.right:          # push right first so left is processed first
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


if __name__ == "__main__":
    root = build_tree()
    print("=== BINARY TREE ===")
    print("BFS:", " -> ".join(bfs(root)))
    print("DFS:", " -> ".join(dfs(root)))
