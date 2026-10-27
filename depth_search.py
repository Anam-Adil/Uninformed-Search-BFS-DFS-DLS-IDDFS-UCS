graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}


def dls(node, goal, limit, path):
    if node == goal:
        return "FOUND", path

    cutoff = False

    for child in graph[node]:
        if child not in path:
            if limit > 0:
                status, result = dls(
                    child, goal, limit - 1, path + [child]
                )

                if status == "FOUND":
                    return "FOUND", result

                if status == "CUTOFF":
                    cutoff = True
            else:
                cutoff = True

    if cutoff:
        return "CUTOFF", None

    return "FAILURE", None


def iddfs(start, goal, max_depth):
    for limit in range(max_depth + 1):
        status, path = dls(start, goal, limit, [start])

        print("Limit:", limit, "| Status:", status, "| Path:", path)

        if status == "FOUND":
            return path

        if status == "FAILURE":
            return None

    return None


print("DLS tests:")
for limit in [1, 2, 3, 4]:
    status, path = dls("A", "G", limit, ["A"])
    print("Limit:", limit, "| Status:", status, "| Path:", path)

print("\nIDDFS test with maximum depth 4:")
iddfs("A", "G", 4)