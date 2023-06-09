def depth_first_search_in_adj_list(graph: dict, start: str) -> set:
    visited = {start}
    stack = [start]
    path = [start]

    while stack:
        v = stack.pop()
        visited.add(v)
        for adj in reversed(graph[v]):
            if adj not in visited:
                stack.append(adj)
                path.append(adj)
    return path


def depth_first_search_in_adj_matrix(graph: list, start: tuple) -> set:
    # Check for an empty graph.
    if not graph:
        return []

    rows, cols = len(graph), len(graph[0])
    visited = {start}
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    path = [start]

    def traverse(i, j):
        if (i, j) in visited:
            return

        visited.add((i, j))
        path.append((i,j))
        # Traverse neighbors.
        for direction in directions:
            next_i, next_j = i + direction[0], j + direction[1]
            if 0 <= next_i < rows and 0 <= next_j < cols:
                # Add in your question-specific checks.
                traverse(next_i, next_j)

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
    print(depth_first_search_in_adj_list(graph_adj_list, "A"))
    print(depth_first_search_in_adj_matrix(graph_adj_matrix,(0,0)))
