import heapq
from collections import defaultdict

INF = float("inf")


class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.entry_finder = {}

    def push(self, node, key):
        self.entry_finder[node] = key
        heapq.heappush(self.heap, (key[0], key[1], node))

    def remove(self, node):
        if node in self.entry_finder:
            del self.entry_finder[node]

    def _cleanup(self):
        while self.heap:
            k1, k2, node = self.heap[0]
            if node not in self.entry_finder:
                heapq.heappop(self.heap)
                continue
            if self.entry_finder[node] != (k1, k2):
                heapq.heappop(self.heap)
                continue
            break

    def top_key(self):
        self._cleanup()
        if not self.heap:
            return (INF, INF)
        k1, k2, _ = self.heap[0]
        return (k1, k2)

    def pop(self):
        self._cleanup()
        if not self.heap:
            return (INF, INF), None
        k1, k2, node = heapq.heappop(self.heap)
        if node in self.entry_finder:
            del self.entry_finder[node]
        return (k1, k2), node

    def contains(self, node):
        return node in self.entry_finder


class DStarLite:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.start = start
        self.goal = goal
        self.last = start
        self.km = 0

        self.g = defaultdict(lambda: INF)
        self.rhs = defaultdict(lambda: INF)
        self.open_list = PriorityQueue()
        self.total_nodes_processed = 0

        self.initialize()

    def initialize(self):
        self.g.clear()
        self.rhs.clear()
        self.open_list = PriorityQueue()
        self.km = 0
        self.last = self.start

        self.rhs[self.goal] = 0
        self.open_list.push(self.goal, self.calculate_key(self.goal))

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def in_bounds(self, node):
        r, c = node
        return 0 <= r < self.rows and 0 <= c < self.cols

    def is_blocked(self, node):
        r, c = node
        return self.grid[r][c] == 1

    def cost(self, a, b):
        if not self.in_bounds(a) or not self.in_bounds(b):
            return INF
        if self.is_blocked(a) or self.is_blocked(b):
            return INF
        return 1

    def get_adjacent_cells(self, node):
        r, c = node
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        neighbors = []
        for dr, dc in directions:
            nxt = (r + dr, c + dc)
            if self.in_bounds(nxt):
                neighbors.append(nxt)

        return neighbors

    def get_successors(self, node):
        return [n for n in self.get_adjacent_cells(node) if not self.is_blocked(n)]

    def get_predecessors(self, node):
        return [n for n in self.get_adjacent_cells(node) if not self.is_blocked(n)]

    def calculate_key(self, node):
        best = min(self.g[node], self.rhs[node])
        return (best + self.heuristic(self.start, node) + self.km, best)

    def update_vertex(self, node):
        if node != self.goal:
            successors = self.get_successors(node)
            if successors:
                self.rhs[node] = min(self.cost(node, s) + self.g[s] for s in successors)
            else:
                self.rhs[node] = INF

        if self.open_list.contains(node):
            self.open_list.remove(node)

        if self.g[node] != self.rhs[node]:
            self.open_list.push(node, self.calculate_key(node))

    def compute_shortest_path(self):
        while (self.open_list.top_key() < self.calculate_key(self.start)) or (self.rhs[self.start] != self.g[self.start]):
            k_old, u = self.open_list.pop()

            if u is None:
                break

            k_new = self.calculate_key(u)
            self.total_nodes_processed += 1

            if k_old < k_new:
                self.open_list.push(u, k_new)
            elif self.g[u] > self.rhs[u]:
                self.g[u] = self.rhs[u]
                for pred in self.get_predecessors(u):
                    self.update_vertex(pred)
            else:
                self.g[u] = INF
                self.update_vertex(u)
                for pred in self.get_predecessors(u):
                    self.update_vertex(pred)

    def update_start(self, new_start):
        self.km += self.heuristic(self.last, new_start)
        self.start = new_start
        self.last = new_start

    def add_obstacle(self, cell):
        r, c = cell

        if not self.in_bounds(cell):
            return False
        if self.grid[r][c] == 1:
            return False
        if cell == self.start or cell == self.goal:
            return False

        self.grid[r][c] = 1

        affected = set(self.get_adjacent_cells(cell))
        affected.add(cell)

        for node in affected:
            self.update_vertex(node)

        return True

    def get_best_next_step(self):
        successors = self.get_successors(self.start)
        if not successors:
            return None

        best = None
        best_value = INF

        for s in successors:
            value = self.cost(self.start, s) + self.g[s]
            if value < best_value:
                best_value = value
                best = s

        return best

    def extract_path(self, max_steps=None):
        if max_steps is None:
            max_steps = self.rows * self.cols * 4

        if self.g[self.start] == INF:
            return []

        path = [self.start]
        current = self.start
        visited = set()

        for _ in range(max_steps):
            if current == self.goal:
                return path

            visited.add(current)
            successors = self.get_successors(current)

            if not successors:
                return []

            next_node = None
            best_value = INF

            for s in successors:
                value = self.cost(current, s) + self.g[s]
                if value < best_value:
                    best_value = value
                    next_node = s

            if next_node is None or best_value == INF:
                return []

            if next_node in visited and next_node != self.goal:
                return []

            path.append(next_node)
            current = next_node

        return []