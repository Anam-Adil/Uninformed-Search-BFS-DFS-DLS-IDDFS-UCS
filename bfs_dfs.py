from collections import deque
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}
def bfs(start, goal):
    q = deque([(start, [start])])
    seen = {start}
    visit_order = []
    while q:
        node, path = q.popleft()
        visit_order.append(node)

        if node == goal:
            return path, visit_order

        for n in graph[node]:
            if n not in seen:
                seen.add(n)
                q.append((n, path + [n]))
    return None, visit_order
def dfs(start, goal):
    stack = [(start, [start])]
    seen = set()
    visit_order = []
    while stack:
        node, path = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        visit_order.append(node)
        if node == goal:
            return path, visit_order
        for n in reversed(graph[node]):
            if n not in seen:
                stack.append((n, path + [n]))
    return None, visit_order
print("BFS:", bfs("A", "G"))
print("DFS:", dfs("A", "G"))