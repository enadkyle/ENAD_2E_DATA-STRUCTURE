from collections import deque


class Graph:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        self.adj.setdefault(v, [])

    def add_edge(self, u, v):
        """Undirected edge."""
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append(v)
        self.adj[v].append(u)

    def display(self):
        for vertex, neighbors in self.adj.items():
            print(f"{vertex}: {', '.join(neighbors)}")

    def bfs(self, start):
        visited = {start}
        queue = deque([start])
        order = []
        while queue:
            v = queue.popleft()
            order.append(v)
            for n in self.adj[v]:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)
        return order

    def dfs(self, start):
        visited = set()
        order = []

        def visit(v):
            visited.add(v)
            order.append(v)
            for n in self.adj[v]:
                if n not in visited:
                    visit(n)

        visit(start)
        return order


def build_graph():
    #     E
    #    / \
    #   N---A
    #    \ /
    #     D
    g = Graph()
    for v in ["E", "N", "A", "D"]:
        g.add_vertex(v)
    g.add_edge("E", "N")
    g.add_edge("E", "A")
    g.add_edge("N", "D")   # added before N-A so N's list is E, D, A
    g.add_edge("N", "A")
    g.add_edge("A", "D")
    return g


if __name__ == "__main__":
    g = build_graph()
    print("=== GRAPH ===")
    g.display()
    print("BFS:", " -> ".join(g.bfs("E")))
    print("DFS:", " -> ".join(g.dfs("E")))
