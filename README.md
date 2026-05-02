# Artificial Intelligence Sessional

A collection of lab work, implementations, and assignments from the **Artificial Intelligence Sessional** course. The repository is organized by lab session and covers core AI search algorithms, heuristic methods, and classic problem-solving techniques — all implemented in Python.

---

## Repository Structure

```
Artificial-Intelligence-Sessional/
│
├── Day_1/                          # Python fundamentals & environment setup
│   ├── AiLab_Class_1.ipynb         # Input/output, conditionals, loops, lists
│   ├── python_basics_week1A.ipynb  # Python basics walkthrough
│   └── python_basics_functions_week1A.ipynb  # Functions (4 styles)
│
├── Day_2/                          # Uninformed search
│   └── main.ipynb                  # BFS-based 8-Puzzle solver
│
├── Day_3/                          # Informed search & local search
│   ├── A_Star_algorithm.py         # A* search with Manhattan distance heuristic
│   ├── best_first_search.py        # Greedy Best-First Search (priority queue)
│   ├── best_first_search_greedy.py # Alternative greedy BFS variant
│   ├── simple_hill_climbing_algo.ipynb  # Simple Hill Climbing on 8-Puzzle
│   └── Steepest Ascent Hill Climbing.py # Steepest Ascent HC with visualization
│
├── Evaluation Preparation/         # Practice problems for lab evaluation
│   ├── main.py                     # BFS & DFS implementations (commented variants)
│   ├── (BFS).py                    # BFS traversal
│   ├── DFS.py                      # DFS traversal
│   ├── Connected_Components.py     # Finding connected components in a graph
│   ├── cycle_detection.py          # Graph cycle detection
│   ├── Shortest Path in Unweighted Graph (BFS).py
│   ├── Maze_Grid Traversal.py      # Grid-based maze traversal
│   ├── maze_solving_with_bfs.py    # BFS-based maze solver
│   ├── rat_in_a_maze.py            # Rat in a Maze backtracking problem
│   └── social_network_problem.py   # Graph problem on social networks
│
├── Evaluation/
│   └── Day_02_Evaluation.ipynb     # Lab evaluation notebook (Day 2)
│
└── Assignment/
    ├── AI_Sessional_Assignment.pdf                  # Assignment problem statement
    └── AI_Sessional_Assignment_202214054.py         # Missionaries & Cannibals BFS solution
```

---

## Topics Covered

| Session | Topic | Key Concepts |
|---|---|---|
| Day 1 | Python Refresher | I/O, control flow, lists, functions |
| Day 2 | Uninformed Search | BFS, 8-Puzzle problem |
| Day 3 | Informed & Local Search | A\*, Best-First Search, Hill Climbing |
| Evaluation Prep | Graph Algorithms | BFS, DFS, cycle detection, maze solving |
| Assignment | Classical AI Problem | Missionaries & Cannibals (BFS) |

---

## Algorithms Implemented

### Search Algorithms
- **BFS (Breadth-First Search)** — graph traversal, shortest path in unweighted graphs, maze solving
- **DFS (Depth-First Search)** — graph traversal, cycle detection
- **Best-First Search** — heuristic-guided search using a priority queue
- **A\* Search** — optimal pathfinding using `f(n) = g(n) + h(n)` with Manhattan distance heuristic

### Local Search
- **Simple Hill Climbing** — applied to the 8-Puzzle using misplaced tiles heuristic
- **Steepest Ascent Hill Climbing** — explores all neighbors and moves to the steepest improvement; includes matplotlib visualization

### Classic AI Problems
- **8-Puzzle** — solved via BFS (uninformed) and Hill Climbing (heuristic)
- **Missionaries & Cannibals** — state-space BFS solution with constraint checking
- **Maze Traversal** — grid-based BFS and backtracking approaches
- **Rat in a Maze** — recursive backtracking

---

## Getting Started

### Prerequisites

- Python 3.8+
- Jupyter Notebook / JupyterLab
- Required libraries:
  ```bash
  pip install numpy matplotlib
  ```

### Running the Notebooks

```bash
jupyter notebook
```

Then open any `.ipynb` file from the relevant day's folder.

### Running the Python Scripts

```bash
python Day_3/A_Star_algorithm.py
python Assignment/AI_Sessional_Assignment_202214054.py
```

---

## Assignment — Missionaries & Cannibals

The assignment implements a BFS solution to the classic **Missionaries and Cannibals** problem:

- **Start state:** 3 missionaries, 3 cannibals, boat on the left bank `(3, 3, 0)`
- **Goal state:** All transferred to the right bank `(0, 0, 1)`
- **Constraint:** Cannibals must never outnumber missionaries on either bank

The solution performs a BFS over all valid states and prints the step-by-step path to the goal.

---

