import heapq

def dijkstra_shortest_path_in_weighted_graph(graph: dict, start: str, end: str) -> int:
    heap = [(0, start)]  # cost from start node,end node
    visited = set({})
    path = []
    while heap:
        (cost, u) = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        path.append(u)
        if u == end:
            return (path, cost)
        for v, c in graph[u]:
            if v in visited:
                continue
            next = cost + c
            heapq.heappush(heap, (next, v))

    return -1


if __name__ == "__main__":
    graph_adj_list = {
        "A": [["B", 2], ["C", 5]],
        "B": [["A", 2], ["D", 3], ["E", 1], ["F", 1]],
        "C": [["A", 5], ["F", 3]],
        "D": [["B", 3]],
        "E": [["B", 4], ["F", 3]],
        "F": [["C", 3], ["E", 3]],
    }

    print(dijkstra_shortest_path_in_weighted_graph(graph_adj_list, "A", "F"))
