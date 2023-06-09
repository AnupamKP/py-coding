def get_shortest_path(graph: dict, start, goal) -> str:
    # keep track of visited nodes
    visited = []
    # keep track of all the paths to be checked
    queue = [[start]]

    # return path if start is goal
    if start == goal:
        return start

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in visited:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            # mark node as visited
            visited.append(node)

    # in case there's no path between the 2 nodes
    return -1


def get_shortest_path_distance(graph: dict, start, target) -> int:
    if not graph or start not in graph or target not in graph:
        return -1
    if start == target:
        return 0
    queue = [start]
    visited = [start]
    # Keep tab on distances from `start` node.
    distance = {start: 0, target: -1}
    while queue:
        node = queue.pop(0)
        if node == target:
            distance[target] = (
                distance[node] if distance[target] == -1 else min(distance[target], distance[node])
            )
        for adjacent in graph[node]:
            if adjacent not in visited:
                visited.append(adjacent)
                queue.append(adjacent)
                distance[adjacent] = distance[node] + 1
    return distance[target]


if __name__ == "__main__":
    graph = {
    "A": ["B", "C", "E"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B"],
    "E": ["A", "B", "D"],
    "F": ["C"],
    "G": ["C"],
}
    print(get_shortest_path(graph, "A", "C"))
    print(get_shortest_path_distance(graph, "A", "C"))