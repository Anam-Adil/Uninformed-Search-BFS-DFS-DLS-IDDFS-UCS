from collections import deque
import heapq
weighted_graph = {
    "A": [("B", 1), ("C", 2)],
    "B": [("D", 4), ("E", 1)],
    "C": [("F", 2), ("G", 10)],
    "D": [],
    "E": [("G", 1)],
    "F": [],
    "G": []
}
def bfs(start, goal):
    graph = {
        node: [neighbor for neighbor, cost in edges]
        for node, edges in weighted_graph.items()
    }

    q = deque([(start, [start])])
    seen = {start}

    while q:
        node, path = q.popleft()

        if node == goal:
            return path

        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                q.append((neighbor, path + [neighbor]))

    return None
def ucs(start, goal):
    heap = [(0, 0, start, [start])]
    seen = set()
    order = []
    counter = 1

    while heap:
        cost, _, node, path = heapq.heappop(heap)

        if node in seen:
            continue

        seen.add(node)
        order.append(node)

        if node == goal:
            return path, cost, order

        for neighbor, weight in weighted_graph[node]:
            if neighbor not in seen:
                heapq.heappush(
                    heap,
                    (cost + weight, counter,
                     neighbor, path + [neighbor])
                )
                counter += 1

    return None, float("inf"), order
bfs_path = bfs("A", "G")
bfs_cost = sum(
    next(w for n, w in weighted_graph[u] if n == v)
    for u, v in zip(bfs_path, bfs_path[1:])
)
ucs_path, ucs_cost, order = ucs("A", "G")

print("BFS path:", bfs_path)
print("BFS edges:", len(bfs_path) - 1)
print("BFS cost:", bfs_cost)

print("UCS path:", ucs_path)
print("UCS edges:", len(ucs_path) - 1)
print("UCS cost:", ucs_cost)
print("UCS processing order:", order)