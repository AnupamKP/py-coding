def breadth_first_search_in_adj_list(graph: dict, start: str) -> set:
    visited = {start}
    queue = [start]
    
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in visited:
                visited.add(w)
                queue.append(w)
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
    print(breadth_first_search_in_adj_list(graph_adj_list, "A"))
