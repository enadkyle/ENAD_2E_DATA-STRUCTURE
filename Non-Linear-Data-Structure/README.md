# Non-Linear Data Structure (ENAD)

Assessment 3.3 - program for each diagram (Binary Tree and Graph) with BFS and DFS traversals.

## Files
- `binary_tree.py` - Node class, tree build, BFS (queue), DFS pre-order (stack)
- `graph.py` - undirected Graph (adjacency list), BFS, DFS

## Binary Tree
```
      E
     / \
    N   A
   /
  D
```
BFS: E -> N -> A -> D
DFS: E -> N -> D -> A

Run: `python binary_tree.py`

## Graph
Edges: E-N, E-A, N-A, N-D, A-D

BFS: E -> N -> A -> D
DFS: E -> N -> D -> A

Run: `python graph.py`
