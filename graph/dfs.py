def depth_first_search_in_adj_list(graph: dict, start: str) -> set:
    visited = {start}
    stack = [start]
    
    while stack:
        v = stack.pop()
        visited.add(v)
        for adj in reversed(graph[v]):
            if adj not in visited:
                stack.append(adj)
    return visited

if __name__ == "__main__":
    graph_adj_list = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"]
    }
    print(depth_first_search_in_adj_list(graph_adj_list, "A"))