def count_islands(graph: list) -> int:
    if not graph:
        return 0

    count = 0

    def dfs(graph, i, j):
        if i < 0 or j < 0 or i >= len(graph) or j >= len(graph[0]) or graph[i][j] != '1':
            return
        graph[i][j] = '#'
        dfs(graph, i+1, j)
        dfs(graph, i-1, j)
        dfs(graph, i, j+1)
        dfs(graph, i, j-1)

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == '1':
                dfs(graph, i, j)
                count += 1
    return count


if __name__ == "__main__":
    graph_adj_matrix = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    print(count_islands(graph_adj_matrix))
