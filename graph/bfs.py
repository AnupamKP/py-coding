def breadth_first_search_in_adj_list(graph: dict, start: str) -> set:
    # Check for an empty graph.
    if not graph:
        return []

    visited = {start}
    queue = [start]
    path = [start]

    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in visited:
                visited.add(w)
                queue.append(w)
                path.append(w)
    return path


def breadth_first_search_in_adj_matrix(graph: list, start: tuple) -> set:
    # Check for an empty graph.
    if not graph:
        return []

    rows, cols = len(graph), len(graph[0])
    visited = {start}
    path = [start]
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def traverse(i, j):
        queue = [(i, j)]
        while queue:
            curr_i, curr_j = queue.pop(0)
            if (curr_i, curr_j) not in visited:
                visited.add((curr_i, curr_j))
                path.append((curr_i, curr_j))
                # Traverse neighbors.
                for direction in directions:
                    next_i, next_j = curr_i + \
                        direction[0], curr_j + direction[1]
                    if 0 <= next_i < rows and 0 <= next_j < cols:
                        # Add in your question-specific checks.
                        queue.append((next_i, next_j))

    for i in range(rows):
        for j in range(cols):
            traverse(i, j)

    return path


if __name__ == "__main__":
    graph_adj_list = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"]
    }
    graph_adj_matrix = [
        [0, 1, 1, 0, 0, 0],
        [1, 0, 0, 1, 1, 0],
        [1, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 0]
    ]

    print(breadth_first_search_in_adj_list(graph_adj_list, "A"))
    print(breadth_first_search_in_adj_matrix(graph_adj_matrix, (0, 0)))
