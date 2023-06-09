def convert_adjacent_matrix_to_adjacent_list(graph: list, vertices: list) -> dict:
    result_graph = {}
    for v in vertices:
        result_graph[v] = []

    rows, cols = len(graph), len(graph[0])
    for i in range(rows):
        for j in range(cols):
            if graph[i][j] == 1:
                result_graph[vertices[i]].append(vertices[j])

    return result_graph


if __name__ == "__main__":
    graph_adj_matrix = [
        [0,1,1,0,0,0],
        [1,0,0,1,1,0],
        [1,0,0,0,0,1],
        [0,1,0,0,0,0],
        [0,1,0,0,0,1],
        [0,0,1,0,1,0]
    ]
    print(convert_adjacent_matrix_to_adjacent_list(graph_adj_matrix, ["A","B","C","D","E","F"]))
