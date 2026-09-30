IAI_SLE2
 ## BFS and DFS Route Finding

### 1. Project Title

Route Finding using BFS and DFS in Python

### 2. Course

02AML204 — Introduction to Artificial Intelligence

### 3. Problem Statement

Find a route from a starting location to a destination using two AI search algorithms:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)

The same graph is used for both algorithms so that their search behaviour can be compared.

### 4. Graph Used

The route graph contains the following connections:

A → B
A → C
B → D
B → E
C → F
D → G
E → G
F → G

Where:

- A = Home
- G = College

5. Algorithms

BFS

BFS stands for Breadth-First Search.

It explores the graph level by level and uses a queue.

DFS

DFS stands for Depth-First Search.

It explores one branch deeply before backtracking and uses a stack.

6. Python Implementation

The program contains two main functions:

bfs(graph, start, goal)

and

dfs(graph, start, goal)

The program records:

- Search order
- Route found
- Number of nodes visited

### 7. Example

Starting node:

A

Destination:

G

BFS

Search order:

A → B → C → D → E → F → G

Route:

A → B → D → G

Nodes visited:

7

DFS

Search order:

A → B → D → G

Route:

A → B → D → G

Nodes visited:

4

### 8. BFS vs DFS

Feature| BFS| DFS
Full form| Breadth-First Search| Depth-First Search
Search method| Level by level| Deep first
Data structure| Queue| Stack
Shortest path in unweighted graph| Yes| No guarantee
Example nodes visited| 7| 4

### 9. Profiling using PySpy

PySpy can be used to profile the Python program and observe its execution behaviour.

The main functions to observe are:

bfs()
dfs()

PySpy helps identify where the Python program spends its execution time.

## 10. Conclusion

This project demonstrates route finding as an AI search problem. BFS explores level by level, while DFS explores deeply before backtracking. Both algorithms can find a route from A to G, but they use different search strategies.
