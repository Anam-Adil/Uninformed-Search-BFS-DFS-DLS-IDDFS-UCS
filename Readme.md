# Lab 3: AI Search Algorithms

## Introduction
This lab implements different AI search algorithms in Python to find paths between nodes in a graph.

## Files Included

- `bfs_dfs.py` — Implements Breadth-First Search (BFS) and Depth-First Search (DFS).
- `lab3_depth_search.py` — Implements Depth-Limited Search (DLS) and Iterative Deepening Depth-First Search (IDDFS).
- `lab3_ucs.py` — Implements Uniform Cost Search (UCS) and compares it with BFS on a weighted graph.
- `README.md` — Contains project information and instructions for running the programs.
- `outputs/` — Captured output screenshots or trace files, if included.

## Requirements
- Python 3
- Visual Studio Code (VS Code)

## How to Run

1. Open the project folder in VS Code.
2. Select **Terminal → New Terminal**.
3. Run each Python file using the following commands.

### BFS and DFS

```bash
python bfs_dfs.py
```

### DLS and IDDFS

```bash
python lab3_depth_search.py
```

### UCS and BFS Comparison

```bash
python lab3_ucs.py
```

## Algorithms Covered

- **BFS:** Explores nodes level by level.
- **DFS:** Explores a path deeply before backtracking.
- **DLS:** Searches up to a specified depth limit.
- **IDDFS:** Repeats depth-limited search with increasing depth limits.
- **UCS:** Expands nodes according to the lowest accumulated path cost.

## Learning Outcomes

- Understand graph traversal and pathfinding.
- Compare BFS and DFS.
- Understand depth limits and iterative deepening.
- Compare BFS and UCS on a weighted graph.
- Practice implementing AI search algorithms in Python.

## Conclusion
This lab provides practical experience with fundamental AI search algorithms and their behavior on graphs.

## Author
AI Student